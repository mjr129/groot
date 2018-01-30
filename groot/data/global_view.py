from typing import cast

from os import path

from groot.data.lego_model import LegoModel
from intermake import MENV, PathToVisualisable
from intermake.hosts.console import ConsoleHost
from mhelper import file_helper


__model = cast( LegoModel, None )


def current_status():
    return _current_status()


class _current_status:
    def __init__( self ):
        model = current_model()
        self.file = bool( model.file_name )
        self.align = (not model.components.is_empty and all( x.alignment is not None for x in model.components ))
        self.blast = (len( model.edges ) != 0)
        self.fasta = (len( model.sequences ) != 0 and all( x.site_array for x in model.sequences ))
        self.fusions = (bool( model.fusion_events ))
        self.comps = (len( model.components ) != 0)
        self.trees = (not model.components.is_empty and all( x.tree is not None for x in model.components ))
        self.nrfg = (model.nrfg is not None)
        self.data = self.blast or self.fasta
        self.empty = not self.file and not self.data
        self.num_sequences = len( model.sequences )
        self.num_components = len( model.components )
        self.num_alignments = sum( len( x.minor_subsequences ) for x in model.components if x.alignment )
        self.num_trees = sum(1 for x in model.components if x.tree)
        self.num_fusions = len(model.fusion_events)


def current_model() -> LegoModel:
    return __model


def set_model( model ):
    global __model
    __model = model
    MENV.root = model
    
    if isinstance( MENV.host, ConsoleHost ):
        MENV.host.browser_path = PathToVisualisable.root_path( MENV.root )
    
    return __model


def new_model():
    set_model( LegoModel() )


new_model()


def get_samples():
    """
    INTERNAL
    Obtains the list of samples
    """
    sample_data_folder = get_sample_data_folder()
    return file_helper.sub_dirs( sample_data_folder )


def get_sample_data_folder():
    """
    PRIVATE
    Obtains the sample data folder
    """
    return path.join( file_helper.get_directory( __file__, 2 ), "sampledata" )
