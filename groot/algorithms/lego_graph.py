from typing import Iterable, Set, Tuple, FrozenSet, Union, AbstractSet, List

import itertools

from groot.algorithms.classes import FusionPoint
from groot.data.lego_model import LegoSequence, ILeaf
from mgraph import MNode, MGraph, FollowParams
from mhelper import ansi, TTristate


_TGetSequences = Union[Iterable[MNode], FollowParams]


class Split:
    """
    Defines an edge in a tree.
    """
    
    
    def __init__( self, inside: FrozenSet[ILeaf], outside: FrozenSet[ILeaf] ):
        """
        CONSTRUCTOR
        :param inside:      Nodes inside the edge 
        :param outside:     Node outside the edge 
        """
        self.inside: FrozenSet[ILeaf] = inside
        self.outside: FrozenSet[ILeaf] = outside
        self.all = frozenset( itertools.chain( self.inside, self.outside ) )
    
    
    def intersection( self, other: AbstractSet[ILeaf] ) -> "Split":
        """
        Returns a split that encompasses the intersection of this split and an `other`.
        """
        return Split( frozenset( self.inside.intersection( other ) ),
                      frozenset( self.outside.intersection( other ) ) )
    
    
    def is_redundant( self ) -> bool:
        """
        A split is bad if it has no nodes on one side of the edge.
        """
        return not self.inside or not self.outside
    
    
    def __str__( self ):
        """
        OVERRIDE 
        """
        r = []
        
        for x in sorted( self.all, key = str ):
            if x in self.inside:
                r.append( ansi.FORE_GREEN + str( x ) + ansi.FORE_RESET )
            else:
                r.append( ansi.FORE_RED + str( x ) + ansi.FORE_RESET )
        
        return "·".join( r )
        
        # return string_helper.format_array( self.all, sort = True )+" = "+ ansi.FORE_GREEN + string_helper.format_array( self.inside, sort = True ) + ansi.RESET + " ¦ " + ansi.FORE_RED + string_helper.format_array( self.outside, sort = True ) + ansi.RESET
    
    
    @property
    def is_empty( self ):
        """
        A split is empty if it has no inside nodes.
        TODO: Is this a bad use case of is_redundant?
        """
        return len( self.inside ) == 0
    
    
    def is_evidenced_by( self, other: "Split" ) -> TTristate:
        """
        A split is evidenced by an `other` if it is a subset of the `other`.
        No evidence can be provided if the `other` set of leaves is not a subset 
        """
        if not self.all.issubset( other.all ):
            return None
        
        return self.inside.issubset( other.inside ) and self.outside.issubset( other.outside )
    
    
    def __len__( self ):
        """
        Number of inside nodes.
        """
        return len( self.inside )
    
    
    def __hash__( self ):
        """
        OVERRIDE
        Hash of the split. See `__eq__`.
        """
        return hash( (self.inside, self.outside) )
    
    
    def __eq__( self, other ):
        """
        OVERRIDE
        Splits are equal if they share the same inside and outside nodes.
        """
        return isinstance( other, Split ) and self.inside == other.inside and self.outside == other.outside


def get_sequences( nodes: Iterable[MNode] ) -> Set[LegoSequence]:
    return set( node.data for node in nodes if isinstance( node.data, LegoSequence ) )


def get_fusions( nodes: Iterable[MNode] ) -> Set[FusionPoint]:
    return set( node.data for node in nodes if isinstance( node.data, FusionPoint ) )


def get_fusion_nodes( nodes: Iterable[MNode] ) -> List[MNode]:
    return [node for node in nodes if isinstance( node.data, FusionPoint )]


def is_clade( node: MNode ) -> bool:
    return node.data is None or isinstance( node.data, str )


def is_fusion( node: MNode ) -> bool:
    return isinstance( node.data, FusionPoint )


def get_split_leaves( params: _TGetSequences ) -> Set[ILeaf]:
    if isinstance( params, FollowParams ):
        params = params.visited_nodes
    
    result: Set[ILeaf] = set()
    
    for node in params:
        if isinstance( node.data, LegoSequence ):
            result.add( node.data )
        elif isinstance( node.data, ILeaf ):
            result.add( node.data )
    
    return result


def __iter_splits( graph: MGraph ) -> Iterable[Tuple[FrozenSet[LegoSequence], FrozenSet[LegoSequence]]]:
    """
    Obtains the set of splits in a graph.
    """
    all_sequences = get_split_leaves( graph.nodes )
    
    for edge in graph.edges:
        left_leaves = get_split_leaves( graph.follow( FollowParams( start = edge.left, exclude_edges = [edge] ) ) )
        right_leaves = all_sequences - left_leaves
        yield frozenset( left_leaves ), frozenset( right_leaves )


def get_splits( graph: MGraph ) -> Set[Split]:
    """
    Obtains the set of splits in a graph.
    """
    all_splits: Set[Split] = set()
    
    for left_sequences, right_sequences in __iter_splits( graph ):
        all_splits.add( Split( left_sequences, right_sequences ) )
        all_splits.add( Split( right_sequences, left_sequences ) )
    
    return all_splits