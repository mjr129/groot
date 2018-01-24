import inspect
from collections import defaultdict
from typing import Callable, Iterable, List, Optional, Set, TypeVar

import pyperclip
import re

from groot.algorithms import components, fastaiser, graph_viewing, external_tools, userdomains
from groot.algorithms.classes import FusionPoint
from groot.data import global_view
from groot.data.lego_model import LegoComponent, ILegoVisualisable
from groot.extensions import ext_files, ext_generating
from groot.frontends import ete_providers
from groot.frontends.cli import cli_view_utils
from groot.frontends.gui.gui_view_support import EDomainFunction
from groot.frontends.gui.gui_view_utils import EChanges
from intermake import MCMD, MENV, Plugin, Table, Theme, command, help_command, visibilities
from mgraph import MGraph
from mhelper import ByRef, Filename, MEnum, MOptional, SwitchError, ansi, file_helper, string_helper


__mcmd_folder_name__ = "Viewing"

T = TypeVar( "T" )


@help_command( names = ["algorithm_help", "print_algorithms", "algorithms"] )
def algorithm_help():
    """
    Prints available algorithms.
    """
    r = []
    d = defaultdict( list )
    
    for x, xv in external_tools.__dict__.items():
        if not x.startswith( "_" ) and "_" in x and inspect.isfunction( xv ):
            y = x.split( "_", 1 )
            d[y[0]].append( (y[1], xv) )
    
    for k, v in sorted( d.items(), key = lambda x: x[0] ):
        r.append( "" )
        r.append( Theme.TITLE + "========== " + k + " ==========" + Theme.RESET )
        
        for name, function in v:
            if name != "default":
                r.append( "    " + Theme.COMMAND_NAME + name + Theme.RESET )
                r.append( "    " + (function.__doc__ or "").strip() )
                r.append( "" )
        
        r.append( "" )
    
    return "\n".join( r )


@command( names = ["print_fasta", "fasta"] )
def print_fasta( target: ILegoVisualisable ) -> EChanges:
    """
    Presents the FASTA sequences for an object.
    :param target:   Object to present.
    """
    MCMD.information( cli_view_utils.colour_fasta_ansi( fastaiser.to_fasta( target ), global_view.current_model().site_type ) )
    return EChanges.INFORMATION


@command( names = ["print_status", "status"], highlight = True )
def print_status() -> EChanges:
    """
    Prints the status of the model. 
    :return: 
    """
    model = global_view.current_model()
    
    p = ByRef[bool]( False )
    r = []
    r.append( Theme.HEADING + "Model" + Theme.RESET )
    r.append( "Project name:  {}".format( __get_status_line_comment( bool( model.sequences ), p, ext_files.import_blast, model.name ) ) )
    r.append( "File name:     {}".format( __get_status_line_comment( model.file_name is not None, p, ext_files.file_save, model.file_name if model.file_name else "Unsaved" ) ) )
    r.append( "" )
    r.append( Theme.HEADING + "Sequences" + Theme.RESET )
    r.append( "Sequences:     {}".format( __get_status_line( p, model.sequences, lambda _: True, ext_files.import_blast ) ) )
    r.append( "FASTA:         {}".format( __get_status_line( p, model.sequences, lambda x: x.site_array, ext_files.import_fasta ) ) )
    r.append( "Components:    {}".format( __get_status_line( p, model.sequences, lambda x: model.components.has_sequence( x ), ext_generating.make_components ) ) )
    r.append( "" )
    r.append( Theme.HEADING + "Components" + Theme.RESET )
    r.append( "Components:    {}".format( __get_status_line( p, model.components, lambda x: True, ext_generating.make_components ) ) )
    r.append( "Alignments:    {}".format( __get_status_line( p, model.components, lambda x: x.alignment, ext_generating.make_alignments ) ) )
    r.append( "Trees:         {}".format( __get_status_line( p, model.components, lambda x: x.tree, ext_generating.make_trees ) ) )
    r.append( "" )
    r.append( Theme.HEADING + "NRFG" + Theme.RESET )
    r.append( "Fusion points: {}".format( __get_status_line( p, [model], lambda x: x.fusion_events, ext_generating.make_fusions ) ) )
    r.append( "Fusion graph : {}".format( __get_status_line( p, [model], lambda x: x.nrfg, ext_generating.make_nrfg ) ) )
    MCMD.print( "\n".join( r ) )
    return EChanges.INFORMATION


@command( names = ["print_alignments", "alignments"] )
def print_alignments( component: Optional[List[LegoComponent]] = None ) -> EChanges:
    """
    Prints the alignment for a component.
    :param component:   Component to print alignment for. If not specified prints all alignments.
    """
    to_do = cli_view_utils.get_component_list( component )
    m = global_view.current_model()
    
    for component_ in to_do:
        MCMD.print( __print_header( component_ ) )
        if component_.alignment is None:
            raise ValueError( "No alignment is available for this component. Did you remember to run `align` first?" )
        else:
            MCMD.information( cli_view_utils.colour_fasta_ansi( component_.alignment, m.site_type, m ) )
    
    return EChanges.INFORMATION


class EFormat( MEnum ):
    """
    :data NEWICK:       Newick format
    :data ASCII:        Simple ASCII diagram
    :data ETE_GUI:      Interactive diagram, provided by Ete. Is also available in CLI. Requires Ete.
    :data ETE_ASCII:    ASCII, provided by Ete. Requires Ete.
    :data SVG:          SVG graphic
    :data HTML:         HTML graphic
    :data CSV:          Excel-type CSV with headers, suitable for Gephi.
    :data DEBUG:        Debug format. Reflects source data and not the tree.
    """
    NEWICK = 1
    ASCII = 2
    ETE_GUI = 3
    ETE_ASCII = 4
    SVG = 5
    HTML = 6
    CSV = 7
    DEBUG = 8


class EOut( MEnum ):
    """
    Output mode.
    
    :data DEFAULT: Same as NORMAL, unless a filename is specified, in which this is the same as FILE.
    :data NORMAL:  Display in current UI
    :data STDOUT:  Write to STDOUT regardless of current UI.
    :data CLIP:    Write to clipboard.
    :data FILE:    Write to file. 
    """
    DEFAULT = 0
    NORMAL = 1
    STDOUT = 2
    CLIP = 3
    FILE = 4


@command( names = ["print_consensus", "consensus"] )
def print_consensus( component: Optional[List[LegoComponent]] = None ) -> EChanges:
    """
    Prints the consensus tree for a component.
    See also `print_trees`, which permits more advanced options.
    
    :param component:   Component to print. If not specified prints all trees.
    """
    print_trees( component = component, consensus = True )
    
    return EChanges.INFORMATION


@help_command()
def print_trees_help() -> str:
    """
    Help on tree-node formatting.
    """
    r = ["The following substitutions are made in the node format string.", ""]
    
    for method_name in dir( graph_viewing.FORMATTER ):
        if not method_name.startswith( "_" ) and callable( getattr( graph_viewing.FORMATTER, method_name ) ):
            r.append( "`[{}]`".format( method_name ) )
            doc = (getattr( graph_viewing.FORMATTER, method_name ).__doc__ or "Not documented :(").strip()
            r.extend( doc.split( "\n" ) )
    
    for i in range( len( r ) ):
        r[i] = r[i].strip()
    
    return "\n".join( r )


@command( names = ["print_trees", "trees", "print_tree", "tree"] )
def print_trees( graph: Optional[MGraph] = None,
                 view: EFormat = EFormat.ASCII,
                 format: str = None,
                 out: EOut = EOut.DEFAULT,
                 file: MOptional[Filename] = None ) -> EChanges:
    """
    Prints the tree for a component.
    
    :param file:        File to write the output to.
    :param out:         Output. Ignored if `file` is set.
    :param graph:       What to print. Prints everything if not specified.
    :param format:      How to format the nodes. See `print_trees_help`.
    :param view:        How to view the tree.
    """
    formatter = graph_viewing.create_user_formatter( format )
    model = global_view.current_model()
    trees = []
    
    if file:
        if out not in (EOut.DEFAULT, EOut.FILE):
            raise ValueError( "Cannot specify both the `out` and `file` parameters." )
        
        out = EOut.FILE
    elif out == EOut.DEFAULT:
        out = EOut.NORMAL
    
    if graph is None:
        for component_ in model.components:
            if component_.tree:
                trees.append( (str( component_ ), component_.tree) )
        
        if model.nrfg:
            trees.append( (str( "NRFG" ), model.nrfg) )
    else:
        trees.append( ("", graph) )
    
    text = []
    
    for name, tree in trees:
        if len( trees ) != 1:
            text.append( __print_header( name ) )
        
        if tree is None:
            MCMD.print( "I cannot draw this tree because it has not yet been generated." )
            continue
        
        if view == EFormat.ASCII:
            text.append( tree.to_ascii( formatter ) )
        elif view == EFormat.ETE_ASCII:
            text.append( ete_providers.tree_to_ascii( tree, model, formatter ) )
        elif view == EFormat.DEBUG:
            text.append( __tree_to_debug( model, tree ) )
        elif view == EFormat.NEWICK:
            text.append( tree.to_newick( formatter ) )
        elif view == EFormat.ETE_GUI:
            ete_providers.show_tree( tree, model, formatter )
        elif view == EFormat.SVG:
            text.append( tree.to_svg( formatter ) )
        elif view == EFormat.HTML:
            text.append( tree.to_svg( formatter, html = True ) )
        elif view == EFormat.CSV:
            text.append( tree.to_csv( formatter ) )
        else:
            raise SwitchError( "view", view )
    
    text = "\n".join( text )
    
    if out == EOut.NORMAL:
        MCMD.information( text )
    elif out == EOut.STDOUT:
        print( text )
    elif out == EOut.CLIP:
        pyperclip.copy( text )
        MCMD.information( "Output copied to clipboard." )
    elif out == EOut.FILE:
        file_helper.write_all_text( file, text )
    
    return EChanges.INFORMATION


def __tree_to_debug( model, tree ):
    rx = []
    r = re.compile( ":[0-9.]+" )
    for line in tree.import_info:
        line = r.sub( "", line )
        for s in sorted( model.sequences, key = lambda x: -len( str( x.id ) ) ):
            line = line.replace( "S{}".format( s.id ), s.accession )
        rx.append( line )
    rrx = "\n".join( rx )
    return rrx


def __print_header( x ):
    if isinstance( x, LegoComponent ):
        x = "COMPONENT {}".format( x )
    
    return "\n" + Theme.TITLE + "---------- {} ----------".format( x ) + Theme.RESET


@command( names = ["print_interlinks", "interlinks"] )
def print_component_edges( component: Optional[LegoComponent] = None, verbose: bool = False ) -> EChanges:
    """
    Prints the edges between the component subsequences.
    
    Each line is of the form:
    
        `FROM <minor> TO <major> [ <start> : <end> ] <length>`
        
    Where:
    
        `minor`  is the source component
        `major`  is the destination component
        `start`  is the average of the start of the destination entry point
        `end`    is the average of the end of the destination entry point
        `length` is the average length of the sequences in the destination 

    :param component: Component to print. If not specified prints a summary of all components.
    :param verbose:   Print everything!
    """
    model = global_view.current_model()
    
    if not model.components:
        raise ValueError( "Cannot print components because components have not been calculated." )
    
    if verbose:
        message = Table()
        
        if component:
            message.add_title( component )
        else:
            message.add_title( "all components" )
        
        message.add_row( "component", "origins", "destinations" )
        message.add_hline()
        
        for major in model.components:
            assert isinstance( major, LegoComponent )
            
            if component is not None and component is not major:
                continue
            
            major_seq = string_helper.format_array( major.major_sequences, join = "\n" )
            minor_seq = string_helper.format_array( major.minor_subsequences, join = "\n" )
            
            message.add_row( major, major_seq, minor_seq )
        
        MCMD.print( message.to_string() )
    
    message = Table()
    
    if component:
        message.add_title( component )
    else:
        message.add_title( "all components" )
    
    average_lengths = components.get_average_component_lengths( model )
    
    message.add_row( "source", "destination", "sequence", "seq-length", "start", "end", "edge-length" )
    message.add_hline()
    
    for major in model.components:
        if component is not None and component is not major:
            continue
        
        major_sequences = list( major.major_sequences )
        
        for minor in model.components:
            if major is minor:
                continue
            
            start = 0
            end = 0
            failed = False
            
            for sequence in major_sequences:
                # subsequences that are in major sequence is a major sequence of major and are a minor subsequence of minor
                subsequences = [x for x in minor.minor_subsequences if x.sequence is sequence]
                
                if subsequences:
                    start += subsequences[0].start
                    end += subsequences[-1].end
                    
                    if component is not None:
                        message.add_row( minor, major, sequence.accession, sequence.length, subsequences[0].start, subsequences[-1].end, subsequences[-1].end - subsequences[0].start )
                else:
                    failed = True
            
            if failed:
                continue
            
            start /= len( major_sequences )
            end /= len( major_sequences )
            
            message.add_row( minor, major, "AVG*{}".format( len( major_sequences ) ), round( average_lengths[major] ), round( start ), round( end ), round( end - start ) )
    
    MCMD.print( message.to_string() )
    return EChanges.INFORMATION


@command( names = ["print_edges", "edges"] )
def print_edges() -> EChanges:
    """
    Prints model edges
    """
    
    model = global_view.current_model()
    
    for edge in model.edges:
        MCMD.print( str( edge ) )
    
    return EChanges.NONE


@command( names = ["print_sequences", "sequences"] )
def print_sequences( domain: EDomainFunction = EDomainFunction.COMPONENT, parameter: int = 0 ) -> EChanges:
    """
    Prints the sequences (as components)
    
    :param domain:      How to break up the sequences 
    :param parameter:   Parameter on `domain` 
    :return: 
    """
    
    model = global_view.current_model()
    longest = max( x.length for x in model.sequences )
    r = []
    
    for sequence in model.sequences:
        minor_components = model.components.find_components_for_minor_sequence( sequence )
        
        if not minor_components:
            minor_components = [None]
        
        for component_index, component in enumerate( minor_components ):
            if component_index == 0:
                r.append( sequence.accession.ljust( 20 ) )
            else:
                r.append( "".ljust( 20 ) )
            
            if component:
                r.append( cli_view_utils.component_to_ansi( component ) + " " )
            else:
                r.append( "Ø " )
            
            subsequences = userdomains.by_enum( sequence, domain, parameter )
            
            for subsequence in subsequences:
                components = model.components.find_components_for_minor_subsequence( subsequence )
                
                if component in components:
                    colour = cli_view_utils.component_to_ansi_back( component )
                else:
                    colour = ansi.BACK_LIGHT_BLACK
                
                size = max( 1, int( (subsequence.length / longest) * 80 ) )
                name = "{}-{}".format( subsequence.start, subsequence.end )
                
                r.append( colour +
                          ansi.DIM +
                          ansi.FORE_BLACK +
                          "▏" +
                          ansi.NORMAL +
                          string_helper.centre_align( name, size ) )
            
            r.append( Theme.RESET + "\n" )
        
        r.append( "\n" )
    
    MCMD.information( "".join( r ) )
    return EChanges.INFORMATION


@command( names = ["print_components", "components"] )
def print_components( verbose: bool = False ) -> EChanges:
    """
    Prints the major components.
    
    Each line takes the form:
    
        `COMPONENT <major> = <sequences>`
        
    Where:
    
        `major` is the component name
        `sequences` is the list of components in that sequence
        
    :param verbose: Print verbose information
    
    """
    model = global_view.current_model()
    
    if not model.components:
        raise ValueError( "Cannot print major components because components have not been calculated." )
    
    message = Table()
    
    message.add_title( "major elements of components" )
    message.add_row( "component", "major elements" )
    message.add_hline()
    
    for component in model.components:
        message.add_row( component, ", ".join( x.accession for x in component.major_sequences ) )
    
    MCMD.print( message.to_string() )
    
    return EChanges.INFORMATION | print_component_edges( verbose = verbose )


def __get_status_line( warned: ByRef[bool], the_list: Iterable[T], test: Callable[[T], bool], plugin: Plugin ) -> str:
    assert isinstance( plugin, Plugin ), plugin
    total = 0
    filtered = 0
    
    for x in the_list:
        total += 1
        if test( x ):
            filtered += 1
    
    return __get_status_line_comment( filtered and filtered == total, warned, plugin, "{}/{}".format( filtered, total ) )


def __get_status_line_comment( is_done: bool, warned: ByRef[bool], plugin: Optional[Plugin], message ):
    if not is_done:
        if not warned.value and plugin is not None:
            warned.value = True
            return Theme.STATUS_NO + message + Theme.COMMENT + " - Consider running " + Theme.COMMAND_NAME + MENV.host.translate_name( plugin.name ) + Theme.RESET
        else:
            return Theme.STATUS_NO + message + Theme.RESET
    else:
        return Theme.STATUS_YES + message + Theme.RESET


@command( names = ["print_fusions", "fusions"] )
def print_fusions( verbose: bool = False ) -> EChanges:
    """
    Estimates model fusions. Does not affect the model.
    
    :param verbose: Verbose output
    """
    results: List[str] = []
    
    model = global_view.current_model()
    n = 0
    i = False
    
    for fusion_event in model.fusion_events:
        results.append( "{}".format( fusion_event ) )
        results.append( "" )
        
        for fusion_point in fusion_event.points_a:
            __format_fusion_point( fusion_point, results, verbose )
            n += 1
        
        results.append( "" )
        
        for fusion_point in fusion_event.points_b:
            __format_fusion_point( fusion_point, results, verbose )
        
        if len( fusion_event.points_a ) != len( fusion_event.points_b ):
            i = True
        
        results.append( "" )
        results.append( "" )
    
    MCMD.information( "\n".join( results ) )
    
    if n == 0:
        MCMD.information( "Your model contains no fusion events. Have you tried generating some?" )
    elif i:
        MCMD.information( "An agreement on the number of fusion events is not agreed by the trees in your model." )
    elif n == 1:
        MCMD.information( "Your model contains 1 fusion." )
    else:
        MCMD.information( "Your model contains {} fusions.".format( n ) )
    
    return EChanges.INFORMATION


def __format_fusion_point( fusion_point: FusionPoint, results, verbose ):
    if not verbose:
        results.append( "  •  {}".format( str( fusion_point ) ) )
        results.append( "         {} : {}".format( fusion_point.count, ",".join( sorted( str( x ) for x in fusion_point.genes ) ) ) )
        return
    
    results.append( "  •  component         {}".format( fusion_point.component ) )
    results.append( "     component         {}".format( fusion_point.opposite_component ) )
    results.append( "     intersect         {}".format( string_helper.format_array( fusion_point.event.intersections ) ) )
    results.append( "     intersect         {}".format( string_helper.format_array( fusion_point.event.orig_intersections ) ) )
    results.append( "     sequences         {}".format( string_helper.format_array( fusion_point.genes ) ) )
    results.append( "     fusion_node_uid   {}".format( fusion_point.fusion_node_uid ) )


@command( visibility = visibilities.ADVANCED )
def groot():
    """
    Displays the application version.
    """
    MCMD.print( "I AM {}. VERSION {}.".format( MENV.name, MENV.version ) )
