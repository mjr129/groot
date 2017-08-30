from ete3 import Tree

from legoalign import external_runner
from legoalign.LegoModels import LegoComponent
from legoalign.scripts import external_tools


def generate_tree(component : LegoComponent) -> None:
    """
    Creates a tree from the component.
    
    The tree is set as the component's `tree` field. 
    """
    try:
        # noinspection PyUnresolvedReferences
        from mhelper import BioHelper
        # noinspection PyUnresolvedReferences
        from Bio import Phylo
    except ImportError:
        raise ImportError( "Install BioPython if you want to generate NRFGs." )
    
    if component.alignment is None:
        raise ValueError("Cannot generate the tree because the alignment has not yet been specified.")
    
    # Read the result
    component.tree = external_runner.run_in_temporary( external_tools.tree, component.alignment )
    
    # Fix the sequence names
    for sequence in component.minor_sequences():
        if "?" not in sequence.site_array:
            component.tree = component.tree.replace( "S{}:".format( sequence.id ), sequence.accession + ":" )
    
    
def tree_from_newick(newick:str)->Tree:
    if "FUSION" in newick:
        return Tree(newick, format=1)
    else:
        return Tree(newick, format=0)
    