"""
Functions that actually edit the model.

In order to maintain correct within-model relationships, the model should only be edited via these functions.
"""

from typing import List, Iterable
from uuid import uuid4

from groot.data.lego_model import LegoModel, LegoSequence, LegoSubsequence, LegoEdge
from mhelper import Logger, array_helper


LOG = Logger( False )
LOG_MAKE_SS = Logger( "make.subsequence", False )


def make_sequence( model: LegoModel,
                   accession: str,
                   obtain_only: bool,
                   initial_length: int,
                   extra_data: object,
                   no_fresh: bool ) -> LegoSequence:
    """
    Creates the specified sequence, or returns it if it already exists.
    """
    assert_model_freshness( model, no_fresh )
    
    assert isinstance( initial_length, int )
    
    if "|" in accession:
        accession = accession.split( "|" )[3]
    
    if "." in accession:
        accession = accession.split( ".", 1 )[0]
    
    accession = accession.strip()
    
    result = None
    
    for sequence in model.sequences:
        if sequence.accession == accession:
            result = sequence
    
    if result is None and not obtain_only:
        result = LegoSequence( model, accession, model._get_incremental_id() )
        model.sequences.add( result )
    
    if result is not None:
        result._ensure_length( initial_length )
        result.comments.append( extra_data )
    
    return result


def make_edge( model: LegoModel, source: LegoSubsequence, destination: LegoSubsequence, extra_data, no_fresh: bool ) -> LegoEdge:
    """
    Creates the specified edge, or returns it if it already exists.
    """
    assert_model_freshness( model, no_fresh )
    
    assert source != destination
    
    for edge in model.edges:
        if (edge.left == source and edge.right == destination) \
                or (edge.left == destination and edge.right == source):
            edge.comments.append( extra_data )
            return edge
    
    result = LegoEdge( source, destination )
    result.comments.append( extra_data )
    model.edges.add( result )
    
    return result


def unlink_all_edges( model: LegoModel, edge: LegoEdge, no_fresh: bool ):
    """
    Removes all references to this edge.
    """
    assert_model_freshness( model, no_fresh )
    
    for x in edge.left:
        x.edges.remove( edge )
    
    for x in edge.right:
        x.edges.remove( edge )
    
    edge.is_destroyed = True


def unlink_edge( edge: LegoEdge, subsequence: "LegoSubsequence", no_fresh: bool ):
    """
    Removes the specified subsequence from the edge.
    
    Warning: If this empties the edge, the edge is automatically destroyed.
    """
    assert_model_freshness( subsequence.sequence.model, no_fresh )
    
    the_list = edge.right if edge.position( subsequence ) else edge.left
    
    subsequence.edges.remove( edge )
    the_list.remove( subsequence )
    
    if len( the_list ) == 0:
        unlink_all_edges( subsequence.sequence.model, edge, no_fresh )



def merge_subsequences( model: LegoModel, all: Iterable[LegoSubsequence], no_fresh: bool ):
    assert_model_freshness( model, no_fresh )
    
    all = sorted( all, key = lambda x: x.start )
    
    if len( all ) <= 1:
        raise ValueError( "Cannot merge a list '{}' of less than two elements.".format( all ) )
    
    for left, right in array_helper.lagged_iterate( all ):
        if left.sequence != right.sequence:
            raise ValueError( "merge_subsequences attempted but the subsequences '{}' and '{}' are not in the same sequence.".format( left, right ) )
        
        if right.start != left.end + 1:
            raise ValueError( "merge_subsequences attempted but the subsequences '{}' and '{}' are not adjacent.".format( left, right ) )
    
    first = all[0]
    first.end = all[-1].end
    
    for other in all[1:]:
        __inherit_subsequence( first, other, no_fresh )
        other.sequence.subsequences.remove( other )
        __destroy_subsequence( other, no_fresh )


def __destroy_subsequence( subsequence: LegoSubsequence, no_fresh: bool ):
    LOG( "DESTROY SUBSEQUENCE {}".format( subsequence ) )
    
    for edge in list( subsequence.edges ):
        unlink_edge( edge, subsequence, no_fresh )
    
    assert len( subsequence.edges ) == 0, subsequence.edges
    subsequence.is_destroyed = True


def add_new_sequence( model: LegoModel, no_fresh: bool ) -> LegoSequence:
    """
    Creates a new sequence
    """
    assert_model_freshness( model, no_fresh )
    return make_sequence( model, str( uuid4() ), False, 10, "user-created", no_fresh )


def add_new_edge( left: LegoSubsequence, right: LegoSubsequence, no_fresh: bool ) -> LegoEdge:
    """
    Creates a new edge between the specified subsequences.
    The specified subsequences should span two, and only two, sequences.
    """
    assert_model_freshness( left.sequence.model, no_fresh )
    
    edge = LegoEdge( left, right )
    left.sequence.model.edges.add( edge )
    
    return edge




def remove_sequences( sequences: List[LegoSequence], no_fresh: bool ):
    """
    Removes the specified sequences
    """
    assert_model_freshness( sequences[0].model, no_fresh )
    
    for sequence in sequences:
        for subsequence in sequence.subsequences:
            __destroy_subsequence( subsequence, no_fresh )
        
        sequence.model.sequences.remove( sequence )


def assert_model_freshness( model, no_fresh: bool ):
    if no_fresh:
        return
    
    if not model.components.is_empty:
        raise ValueError( "Refusing to modify the model whilst it is in use. Did you mean to drop the components first?" )
    
    if model.fusion_events:
        raise ValueError( "Refusing to modify the model whilst it is in use. Did you mean to drop the fusion_events first?" )
    
    if model.nrfg:
        raise ValueError( "Refusing to modify the model whilst it is in use. Did you mean to drop the NRFG first?" )


def remove_edges( subsequences: List[LegoSubsequence], edges: List[LegoEdge], no_fresh: bool ):
    """
    Removes the specified edges from the specified subsequences
    """
    assert_model_freshness( subsequences[0].sequence.model, no_fresh )
    
    for subsequence in subsequences:
        for edge in edges:
            if not edge.is_destroyed:
                unlink_edge( edge, subsequence, no_fresh )
