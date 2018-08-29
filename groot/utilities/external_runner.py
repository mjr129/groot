import os
import shutil
from uuid import uuid4

import groot.data.config
from groot.data import global_view
from intermake.engine import constants
from intermake.engine.environment import MENV, MCMD
from mhelper import file_helper


def run_in_temporary( function, *args, **kwargs ):
    """
    Sets the working directory to a temporary folder inside the current working directory.
    Calls `function`
    Then deletes the temporary folder and returns to the original working directory. 
    """
    temp_folder_name = os.path.join( MENV.local_data.local_folder( constants.FOLDER_TEMPORARY ), "generate-tree" )
    
    if os.path.exists( temp_folder_name ):
        shutil.rmtree( temp_folder_name )
    
    file_helper.create_directory( temp_folder_name )
    os.chdir( temp_folder_name )
    
    try:
        return function( *args, **kwargs )
    except Exception:
        for file in file_helper.list_dir( "." ):
            MCMD.print( "*** DUMPING FILE BECAUSE AN ERROR OCCURRED: {} ***".format( file ) )
            for index, line in enumerate( file_helper.read_all_lines( file ) ):
                MCMD.print( "LINE {}: {} ".format( index, line ) )
            MCMD.print( "*** END OF FILE ***" )
        
        raise
    finally:
        os.chdir( ".." )
        if groot.data.config.options().debug_external_tool:
            nfn = temp_folder_name + "_" + str( uuid4() )[:4]
            os.rename( temp_folder_name, nfn )
            MCMD.warning( "The directory '{}' has not been deleted because of the `debug_external_tool` flag.".format( nfn ) )
        else:
            shutil.rmtree( temp_folder_name )
