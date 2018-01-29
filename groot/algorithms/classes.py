from typing import List, Set, Tuple

from groot.data.lego_model import LegoComponent, LegoSequence
from mgraph import MGraph
from mhelper import array_helper, string_helper


_FusionPoint_ = "FusionPoint"


class NotCommensurateError( Exception ):
    pass


class IFusion:
    pass


class FusionEvent( IFusion ):
    """
    Describes a fusion event
    
    :data component_a:          First component
    :data component_b:          Second component
    :data products:        Generated component (root)
    :data future_products:   Generated component (all possibilities)
    :data point_a:              The name of the node on the first component which the fusion occurs
    :data point_b:              The name of the node on the second component which the fusion occurs
    """
    
    
    def __init__( self, index: int, component_a: LegoComponent, component_b: LegoComponent, intersections: Set[LegoComponent] ) -> None:
        if component_a is component_b:
            raise ValueError( "FusionEvent component A ({}) cannot be component B ({}).".format( component_a, component_b ) )
        
        if any( x is component_a or x is component_b for x in intersections ):
            raise ValueError( "FusionEvent intersections ({}) cannot contain component A ({}) or component B ({}).".format( string_helper.format_array( intersections ), component_a, component_b ) )
        
        self.index = index
        self.component_a: LegoComponent = component_a
        self.component_b: LegoComponent = component_b
        self.products: Set[LegoComponent] = intersections
        self.future_products: Set[LegoComponent] = set( intersections )
        self.points: List[FusionPoint] = None
    
    
    def get_commensurate_points( self ) -> List[Tuple[_FusionPoint_, _FusionPoint_]]:
        """
        Gets tuples of points that look like they are commensurate, or raises a `NotCommensurateError`. 
        """
        if len( self.points_a ) != len( self.points_b ):
            raise NotCommensurateError( "The two sets of fusion points for this event are not the same length, so at least one will be non-commensurate.".format( len( self.points_a ), len( self.points_b ) ) )
        
        results = []
        
        for point_a in self.points_a:
            found = False
            for point_b in self.points_b:
                if point_a.genes == point_b.genes:
                    if found:
                        raise NotCommensurateError( "In the fusion point A there are multiple commensurate points in the B set. A = «{}», B = «{}».".format( point_a, self.points_b ) )
                    
                    results.append( (point_a, point_b) )
                    found = True
            
            if not found:
                raise NotCommensurateError( "In the fusion point A there is no commensurate point in the B set. A = «{}», B = «{}».".format( point_a, self.points_b ) )
        
        return results
    
    
    @property
    def component_c( self ) -> LegoComponent:
        return array_helper.single_or_error( self.products )
    
    
    def __str__( self ) -> str:
        #return "({}+{}={})".format( self.component_a, self.component_b, ",".join( x.__str__() for x in self.products ) )
        return "{}".format( ",".join( x.__str__() for x in self.products ) )


class FusionPoint( IFusion ):
    def __init__( self, event: FusionEvent, component: LegoComponent ):
        self.event = event
        self.component = component
    
    
    def __repr__( self ):
        return "F:{}".format( self.event )


class NrfgEvent:
    def __init__( self, event: FusionEvent, aπ: FusionPoint, bπ: FusionPoint, aΛ: MGraph, aΔ: MGraph, bΛ: MGraph, bΔ: MGraph, dΔ: MGraph ) -> None:
        self.event = event
        self.aπ = aπ
        self.bπ = bπ
        self.aΛ = aΛ
        self.aΔ = aΔ
        self.bΔ = bΔ
        self.bΛ = bΛ
        self.dΔ = dΔ
