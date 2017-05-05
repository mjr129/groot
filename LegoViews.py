"""
MVC architecture.

Classes that manage the view of the model.
"""
from enum import Enum
from random import randint
from typing import List, Optional, Set, Tuple, Union

from PyQt5.QtCore import QPointF, QRect, QRectF, Qt
from PyQt5.QtGui import QBrush, QColor, QFontMetrics, QKeyEvent, QLinearGradient, QPainter, QPen, QPolygonF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsSceneMouseEvent, QStyleOptionGraphicsItem, QWidget

from LegoModels import LegoEdge, LegoModel, LegoSequence, LegoSubsequence
from MHelper import ArrayHelper, QtColourHelper
from MHelper.CommentHelper import override
from MHelper.ExceptionHelper import SwitchError
from MHelper.QtColourHelper import Colours, Pens


class ESequenceColour(Enum):
        RESET = 1
        RANDOM = 2
        
class EApply(Enum):
        ONE =  1    
        ALL = 2
        EDGES = 3
        
# Order of proteins in piano roll
PROTEIN_TABLE = ArrayHelper.create_index_lookup( "IVLFCMAGTSWYPHEQDNKR" )

# Colour of proteins in piano roll
PROT_COLOURS = { "G": Pens.WHITE, "A": Pens.WHITE, "V": Pens.WHITE, "L": Pens.WHITE, "I": Pens.WHITE,
                 "F": Pens.ORANGE, "Y": Pens.ORANGE, "W": Pens.ORANGE,
                 "C": Pens.YELLOW, "M": Pens.YELLOW,
                 "S": Pens.GREEN, "T": Pens.GREEN,
                 "K": Pens.RED, "R": Pens.RED, "H": Pens.RED,
                 "D": Pens.BLUE, "E": Pens.BLUE,
                 "N": Pens.DARK_ORANGE, "Q": Pens.DARK_ORANGE,
                 "P": Pens.LIGHT_RED }

SIZE_MULTIPLIER                                   = 2
PROTEIN_SIZE                                      = 2
DEFAULT_SEQUENCE_YSEP                             = SIZE_MULTIPLIER * 24
SEQUENCE_HEIGHT                                   = SIZE_MULTIPLIER * (len( PROTEIN_TABLE ) + 2)
TEXT_MARGIN                                       = SIZE_MULTIPLIER * 4

PROTEIN_BG                                        = QBrush( QColor( 0, 0, 0 ) )
PROTEIN_DEFAULT_FG                                = QPen( QColor( 255, 255, 0 ) )

SELECTION_EDGE_LINE                               = QPen( QColor( 0, 0, 0 ) )
SELECTION_EDGE_LINE                                 .setStyle(Qt.DotLine)
FOCUS_LINE                                        = QPen( QColor( 255, 255, 255 ) )
FOCUS_LINE.setStyle(Qt.DashLine)
SELECTION_LINE                                    = QPen( QColor( 0, 0, 255 ) )
SELECTION_FILL                                    = Qt.NoBrush

PAGE_LINE                                         = QPen( QColor( 0, 0, 0 ) )
PAGE_LINE                                           .setStyle( Qt.DashLine )
NO_SEQUENCE_LINE                                  = QPen( QColor( 0, 0, 0 ) )
NO_SEQUENCE_LINE                                    .setStyle( Qt.DashLine )
NO_SEQUENE_BACKWARDS_LINE                         = QPen( QColor( 255, 0, 0 ) )
NO_SEQUENE_BACKWARDS_LINE                                     .setStyle( Qt.DashLine )
NO_SEQUENCE_FILL                                  = QBrush( QColor( 0, 0, 0, alpha  = 32 ) )
TEXT_LINE                                         = QPen( QColor( 128, 128, 128 ) )
POSITION_TEXT                                     = QPen( QColor( 64, 64, 64 ) )
DARK_TEXT                                         = QPen( QColor( 0, 0, 0 ) )
LIGHT_TEXT                                        = QPen( QColor( 255, 255, 255 ) )
SINGLE_COMPONENT_COLOUR                           = QColor( 64, 64, 64 )

# Z-values (draw order)
Z_EDGES                                           = 1
Z_SEQUENCE                                        = 2
Z_FOCUS                                           = 3


class LegoViewOptions:
    def __init__( self ):
        self.colour_blend     = 1            # type:float
        self.toggle_selection = False        # type:bool
        self.y_snap           = True         # type:bool
        self.x_snap           = True         # type:bool
        self.colour_apply     = EApply.EDGES # type:EApply
        self.view_edges       = True         # type:Optional[bool]
        self.view_piano_roll  = None         # type:Optional[bool]
        self.view_names       = True         # type:Optional[bool]
        self.view_positions   = None         # type:Optional[bool]


class ColourBlock:
    def __init__( self, colour: QColor ):
        self.colour = colour
        self.brush = QBrush( colour )
        
        dark_colour = QColor( colour.red() // 2, colour.green() // 2, colour.blue() // 2 )
        self.pen = QPen( dark_colour )
        
        if colour.lightness() > 128:
            self.text = DARK_TEXT
        else:
            self.text = LIGHT_TEXT
    
    
    def blend( self, colour: QColor, amount ):
        new_colour = QtColourHelper.interpolate_colours(self.colour, colour, amount) 
        
        return ColourBlock( new_colour )


class LegoEdgeView:
    def __init__( self, owner: "LegoViewComponent", edge: LegoEdge ):
        self.owner = owner
        self.edge = edge
        
        self.source = [ ] #type:List[LegoViewSubsequence]
        self.destination = [ ] #type:List[LegoViewSubsequence]
        
        for x in edge.source:
            self.source.append( owner.owner.find_ui_element( x ) )
        
        for x in edge.destination:
            self.destination.append( owner.owner.find_ui_element( x ) )
    
    
    
    
    
    def paint( self, painter: QPainter ):
        if not self.source or not self.destination:
            return
        
        view_edges = self.owner.owner.view_model.options.view_edges
        
        if view_edges is None:
            view_edges = any(x.isSelected() for x in self.source + self.destination)
            
        if not view_edges:
            return
        
        if self.source[0].window_rect().top() < self.destination[0].window_rect().top():
            upper = self.source
            lower = self.destination
        else:
            upper = self.destination
            lower = self.source 
        
        upper_points = self.__extract_points( upper, False )
        lower_points = self.__extract_points( lower, True )
        
        upper_colour = QtColourHelper.average_colour( list( x.colour.colour for x in upper ) )
        lower_colour = QtColourHelper.average_colour( list( x.colour.colour for x in lower ) )
        
        left = min( upper_points[0].x(), lower_points[-1].x() )
        right = max( upper_points[-1].x(), lower_points[0].x() )
        top = min( x.y() for x in upper_points )
        bottom = max( x.x() for x in lower_points )
        
        gradient = QLinearGradient( left, top, right, bottom )
        f = QColor( upper_colour )
        f.setAlpha( 64 )
        s = QColor( lower_colour )
        s.setAlpha( 64 )
        gradient.setColorAt( 0, f )
        gradient.setColorAt( 1, s )
        
        brush = QBrush( gradient )
        
        painter.setPen( Qt.NoPen )
        painter.setBrush( brush )
        painter.drawPolygon( QPolygonF( upper_points+lower_points+[upper_points[0]] ) )
    
    def __extract_points(self, the_list, backwards):
        results = []
        
        if not backwards:
            for x in sorted(the_list, key = lambda z: z.window_rect().left()):
                r = x.window_rect() #type:QRect
                results.append(r.bottomLeft())
                results.append(r.bottomRight())
        else:
            for x in sorted(the_list, key = lambda z: -z.window_rect().left()):
                r = x.window_rect() #type:QRect
                results.append(r.topRight())
                results.append(r.topLeft())
                
        return results
    
    def __extract_rect( self, the_list ):
        result = the_list[ 0 ].window_rect()
        
        for x in the_list[ 1: ]:
            r = x.window_rect()
            
            if r.top() < result.top():
                result.setTop( r.top() )
            
            if r.bottom() > result.bottom():
                result.setBottom( r.bottom() )
            
            if r.right() > result.right():
                result.setRight( r.right() )
            
            if r.left() < result.left():
                result.setLeft( r.left() )
        
        return result


class LegoViewComponent:
    """
    Connected component view
    """
    
    
    def __init__( self, owner: "LegoViewAllEdges", subsequence_views: "List[LegoViewSubsequence]" ):
        self.owner = owner
        self.subsequence_views = subsequence_views
        
        if len( subsequence_views ) == 1:
            opaque_colour = SINGLE_COMPONENT_COLOUR
        else:
            opaque_colour = owner.next_colour()
        
        self.colour = ColourBlock( opaque_colour )
        
        edges = set()
        
        for subsequence_view in subsequence_views:
            subsequence_view.component = self
            
            if subsequence_view.colour is None:
                subsequence_view.colour = self.colour
            
            for edge in subsequence_view.subsequence.edges:
                edges.add( edge )
        
        self.edges = [ ]
        
        for edge in edges:
            self.edges.append( LegoEdgeView( self, edge ) )
    
    
    def paint( self, painter: QPainter ):
        for edge_view in self.edges:
            edge_view.paint( painter )


class LegoViewSubsequence( QGraphicsItem ):
    def __init__( self, subsequence: LegoSubsequence, owner_view: "LegoViewSequence", positional_index: int, precursor: "LegoViewSubsequence" ):
        super().__init__()
        
        self.rect = QRectF( 0, 0, subsequence.length * PROTEIN_SIZE, SEQUENCE_HEIGHT )
        
        if not subsequence.ui_position:
            self.setPos( subsequence.start * PROTEIN_SIZE, subsequence.sequence.index * (DEFAULT_SEQUENCE_YSEP + SEQUENCE_HEIGHT) )
        else:
            self.setPos( subsequence.ui_position[ 0 ], subsequence.ui_position[ 1 ] )
        
        if not subsequence.ui_colour:
            self.colour = None  # type:ColourBlock
        else:
            self.colour = ColourBlock( QColor( subsequence.ui_colour ) )
        
        self.setFlag( QGraphicsItem.ItemSendsGeometryChanges, True )
        self.setFlag( QGraphicsItem.ItemIsFocusable, True )
        self.setFlag( QGraphicsItem.ItemIsSelectable, True )
        
        self.subsequence = subsequence
        self.owner_sequence_view = owner_view
        self.index = positional_index
        self.edge_subsequence_views = [ ]  # type:List[LegoViewSubsequence]
        self.precursor = precursor
        self.component = None  # type:LegoViewComponent
        self.mousedown_original_pos = None  # type:QPointF
        self.mousemove_label = None  # type:str
        self.mousemove_snapline = None  # type:Tuple[int,int]
        self.mousedown_move_all = False
        
        self.setZValue(Z_SEQUENCE)
        
    
        
    @property
    def owner_model_view(self):
        return self.owner_sequence_view.owner_model_view
    
    @property
    def options(self):
        return self.owner_model_view.options
    
    
    def update_model( self ):
        self.subsequence.ui_position = self.pos().x(), self.pos().y()
        self.subsequence.ui_colour = self.colour.colour.rgba() if self.colour is not None else None
    
    
    @override
    def boundingRect( self ) -> QRectF:
        return self.rect
    
    
    @override
    def paint( self, painter: QPainter, *args, **kwargs ):
        painter.setBrush( self.colour.brush )
        painter.setPen( SELECTION_LINE if self.isSelected() else self.colour.pen )
        painter.drawRect( self.rect )
        
        
            
        draw_piano_roll = self.options.view_piano_roll
        
        if draw_piano_roll is None:
            draw_piano_roll = self.isSelected()
            
        if draw_piano_roll:
            painter.setPen( Qt.NoPen )
            painter.setBrush(PROTEIN_BG)
            OFFX = SIZE_MULTIPLIER
            painter.drawRect( 0, OFFX, self.rect.width(), len( PROTEIN_TABLE ) * SIZE_MULTIPLIER )
            
            
            
            for i, c in enumerate( self.subsequence.array ):
                pos = PROTEIN_TABLE.get( c )
                
                if pos is not None:
                    painter.setPen( PROT_COLOURS.get( c, PROTEIN_DEFAULT_FG ) )
                    painter.drawEllipse( i * SIZE_MULTIPLIER, pos * SIZE_MULTIPLIER + OFFX, SIZE_MULTIPLIER, SIZE_MULTIPLIER )
        
        painter.setPen( TEXT_LINE )
        
        if self.mousemove_snapline:
            x = self.mousemove_snapline[ 0 ] - self.pos().x()
            y = self.mousemove_snapline[ 1 ] - self.pos().y()
            painter.drawLine( x, self.boundingRect().height() / 2, x, y )
            if not self.mousemove_label.startswith( "<" ):
                x -= QFontMetrics( painter.font() ).width( self.mousemove_label )
            
            if y < 0:
                y = self.rect.top() - TEXT_MARGIN
            else:
                y = self.rect.bottom() + TEXT_MARGIN + QFontMetrics( painter.font() ).xHeight()
            painter.drawText( QPointF( x, y ), self.mousemove_label )
        elif self.mousemove_label:
            painter.drawText( QPointF( self.rect.left() + TEXT_MARGIN, self.rect.top() - TEXT_MARGIN ), self.mousemove_label )
        else:
            
                
            if self.__draw_position(): 
                painter.setPen( POSITION_TEXT )
                
                text = str( self.subsequence.start )
                x = self.rect.left() - QFontMetrics( painter.font() ).width( text ) / 2
                painter.drawText( QPointF( x, self.rect.top() - TEXT_MARGIN ), text )
                
                if not self.__draw_next_sibling_position():
                    text = str( self.subsequence.end )
                    x = self.rect.right() - QFontMetrics( painter.font() ).width( text ) / 2
                    painter.drawText( QPointF( x, self.rect.top() - TEXT_MARGIN ), text )
                
        if self.hasFocus():
            r =  self.rect.adjusted(1,1,-1,-1)
            painter.setPen( FOCUS_LINE )
            painter.setBrush( 0)
            painter.drawRect( r )
            
    def __draw_position( self ):
        result = self.options.view_positions
            
        if result is None:
            result = self.isSelected()
            
        return result
    
    def __draw_next_sibling_position(self):
        ns = self.next_sibling()
        
        if ns is None:
            return False
        
        if not ns.__draw_position():
            return False
        
        return ns.pos().x() == self.window_rect().right()
        
    def next_sibling(self):
        ssvs=self.owner_sequence_view.subsequence_views
        i = ssvs.index(self)
        
        if  i== len(ssvs)-1:
            return None
        
        return ssvs[i+1]
    
    
    def window_rect( self ) -> QRectF:
        return self.boundingRect().translated( self.scenePos() )
    
    
    PROHI = False
    
    
    def keyPressEvent( self, e: QKeyEvent ):        
        if e.key() == Qt.Key_Left:
            my_index = self.owner_sequence_view.subsequence_views.index( self )
            my_index -= 1
            if my_index >= 0:
                self.owner_sequence_view.subsequence_views[ my_index ].setFocus()
        elif e.key() == Qt.Key_Right:
            my_index = self.owner_sequence_view.subsequence_views.index( self )
            my_index += 1
            if my_index < len( self.owner_sequence_view.subsequence_views ):
                self.owner_sequence_view.subsequence_views[ my_index ].setFocus()
        
        self.__apply_colour(e)
    
    def mousePressEvent( self, m: QGraphicsSceneMouseEvent ):
        if m.buttons() & Qt.LeftButton:
            for selected_item in self.owner_sequence_view.owner_model_view.scene.selectedItems():
                selected_item.mousedown_original_pos = selected_item.pos()
                
            enable_toggle_selection = not self.options.toggle_selection == (bool(  (m.modifiers() & Qt.ControlModifier) or  (m.modifiers() & Qt.MetaModifier)))
            
            if not enable_toggle_selection:
                if not self.isSelected():
                    self.owner_sequence_view.owner_model_view.scene.clearSelection()
                
                    self.setSelected(True)
            else:
                self.setSelected(not self.isSelected())
                
            m.accept()
            
    def mouseDoubleClickEvent(self, m:QGraphicsSceneMouseEvent):
        s= self.isSelected()
        for x in self.owner_sequence_view.subsequence_views:
            x.setSelected(s)
            
        m.accept()
            
    def focusInEvent(self, QFocusEvent):
        self.setZValue(Z_FOCUS)
        self.owner_model_view.focus_notification(self)
    
    def focusOutEvent(self, QFocusEvent):
        self.setZValue(Z_SEQUENCE)
    
    
    def snaps( self ):
        for sequence_view in self.owner_sequence_view.owner_model_view.sequence_views:
            for subsequence_view in sequence_view.subsequence_views:
                if subsequence_view is not self:
                    left_snap = subsequence_view.scenePos().x()
                    right_snap = subsequence_view.scenePos().x() + subsequence_view.boundingRect().width()
                    yield left_snap, "Start of {0}".format( subsequence_view.subsequence ), subsequence_view.scenePos().y()
                    yield right_snap, "End of {0}".format( subsequence_view.subsequence ), subsequence_view.scenePos().y()
    
    
    def mouseMoveEvent( self, m: QGraphicsSceneMouseEvent ):
        if m.buttons() & Qt.LeftButton:
            if self.mousedown_original_pos is None:
                return 
            
            new_pos = self.mousedown_original_pos + (m.scenePos() - m.buttonDownScenePos( Qt.LeftButton ))  # type:QPointF
            new_x = new_pos.x()
            new_y = new_pos.y()
            new_x2 = new_x + self.boundingRect().width()
            
            self.mousemove_label = "({0} {1})".format( new_pos.x(), new_pos.y() )
            self.mousemove_snapline = None
            
            x_snap_enabled = self.options.x_snap == (not bool(m.modifiers() & Qt.ControlModifier)) 
            y_snap_enabled = self.options.y_snap == (not bool(m.modifiers() & Qt.AltModifier))
            
            if x_snap_enabled :
                for snap_x, snap_label, snap_y in self.snaps():
                    if (snap_x - 8) <= new_x <= (snap_x + 8):
                        new_x = snap_x
                        self.mousemove_label = "<-- " + snap_label
                        self.mousemove_snapline = snap_x, snap_y
                    elif (snap_x - 8) <= new_x2 <= (snap_x + 8):
                        new_x = snap_x - self.boundingRect().width()
                        self.mousemove_label = snap_label + " -->"
                        self.mousemove_snapline = snap_x, snap_y
            
            if y_snap_enabled:
                yy = (SEQUENCE_HEIGHT + DEFAULT_SEQUENCE_YSEP)
                new_y += yy / 2
                new_y = new_y - new_y % yy
            
            new_pos.setX( new_x )
            new_pos.setY( new_y )
            
            self.setPos( new_pos )
            self.update_model()
            
            delta_x = new_x - self.mousedown_original_pos.x()
            delta_y = new_y - self.mousedown_original_pos.y()
            
            for selected_item in self.owner_sequence_view.owner_model_view.scene.selectedItems():
                if selected_item is not self:
                    selected_item.setPos( selected_item.mousedown_original_pos.x() + delta_x, selected_item.mousedown_original_pos.y() + delta_y )
                    selected_item.update_model()
    
    
    def mouseReleaseEvent( self, m: QGraphicsSceneMouseEvent ):
        self.mousemove_label = None
        self.mousemove_snapline = None
        self.update()
        pass  # suprress default mouse handling implementation

    def __apply_colour( self, e: QKeyEvent ):
        new_colour = KEY_COLOURS.get(e.key())
        
        if new_colour is None:
            return
        
        all = (self.options.colour_apply == EApply.ALL) == (not bool(e.modifiers() & Qt.AltModifier))
        one = (self.options.colour_apply == EApply.ONE) ==  (not bool(e.modifiers() & Qt.ShiftModifier))
        
        self.owner_model_view.change_colours( new_colour, EApply.ALL if all else EApply.ONE if one else EApply.EDGES )
    


class LegoViewSequence:
    """
    Views a sequence
    """
    
    
    def __init__( self, owner_model_view: "LegoViewModel", sequence: LegoSequence ):
        """
        :param owner_model_view: Owning view
        :param sequence: The sequence we are viewing
        """
        
        self.owner_model_view = owner_model_view
        self.sequence = sequence
        self.subsequence_views = [ ]  # type:List[LegoViewSubsequence]
        self._recreate()
        


    def _recreate( self ):
        # Remove existing items
        for x in self.subsequence_views:
            self.owner_model_view.scene.removeItem(x)
            
        # Add new items
        previous_subsequence = None
        for subsequence in self.sequence.subsequences:
            subsequence_view = LegoViewSubsequence( subsequence, self, len( self.subsequence_views ), previous_subsequence )
            self.subsequence_views.append( subsequence_view )
            self.owner_model_view.scene.addItem( subsequence_view )
            previous_subsequence = subsequence_view

class LegoViewAllEdges( QGraphicsItem ):
    def __init__( self, view_model: "LegoViewModel" ):
        super().__init__()
        self.setZValue(Z_EDGES)
        self.__next_colour = -1
        self.view_model = view_model
        self.component_views = [ ]  # type: List[LegoViewComponent]
        
        for connected_component in self.__create_components():
            self.component_views.append( LegoViewComponent( self, connected_component ) )
        
        self.rect = QRectF( 0, 0, 0, 0 )
        
        for sequence_view in view_model.sequence_views:
            for subsequence_view in sequence_view.subsequence_views:
                r = subsequence_view.window_rect()
                
                if r.left() < self.rect.left():
                    self.rect.setLeft( r.left() )
                
                if r.right() > self.rect.right():
                    self.rect.setRight( r.right() )
                
                if r.top() < self.rect.top():
                    self.rect.setTop( r.top() )
                
                if r.bottom() > self.rect.bottom():
                    self.rect.setBottom( r.bottom() )
                    
                for edge in subsequence_view.subsequence.edges:
                    for subsequence in edge.opposite(subsequence_view.subsequence):
                        subsequence_view.edge_subsequence_views.append( self.find_ui_element( subsequence ) )
        
        MARGIN = 128
        self.rect.setTop( self.rect.top() - MARGIN )
        self.rect.setLeft( self.rect.left() - MARGIN )
        self.rect.setBottom( self.rect.bottom() + MARGIN )
        self.rect.setRight( self.rect.right() + MARGIN )
    
    
    def next_colour( self ) -> QColor:
        self.__next_colour += 1
        
        if self.__next_colour >= len( COMPONENT_COLOURS ):
            self.__next_colour = 0
        
        return COMPONENT_COLOURS[ self.__next_colour ]
    
    
    def boundingRect( self ):
        return self.rect
    
    
    def paint( self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: Optional[ QWidget ] = None ) -> None:
        for group in self.component_views:
            group.paint( painter )
        
        painter.setPen( PAGE_LINE )
        painter.setBrush( Qt.NoBrush )
        painter.drawRect( self.rect )
        
        painter.setPen( NO_SEQUENCE_LINE )
        painter.setBrush( NO_SEQUENCE_FILL )
        
        for sequence_view in self.view_model.sequence_views:
            for subsequence_view in sequence_view.subsequence_views:
                # Draw my connection (left)
                if subsequence_view.precursor is None:
                    continue
                
                precursor_rect = subsequence_view.precursor.window_rect()
                my_rect = subsequence_view.window_rect()
                
                if precursor_rect.right() == my_rect.left():
                    continue
                
                if my_rect.left() < precursor_rect.right():
                    painter.drawLine( my_rect.left(), (my_rect.top() - 8), precursor_rect.right(), (precursor_rect.top() - 8) )
                    painter.drawLine( my_rect.left(), (my_rect.bottom() + 8), precursor_rect.right(), (precursor_rect.bottom() + 8) )
                    painter.drawLine( my_rect.left(), (my_rect.top() - 8), my_rect.left(), (my_rect.bottom() + 8) )
                    painter.drawLine( precursor_rect.right(), (precursor_rect.top() - 8), precursor_rect.right(), (precursor_rect.bottom() + 8) )
                else:
                    points = [ QPointF( my_rect.left(), my_rect.top() + 8 ),  # a |x...|
                               QPointF( my_rect.left(), my_rect.bottom() - 8 ),  # b |x...|
                               QPointF( precursor_rect.right(), precursor_rect.bottom() - 8 ),  # b |...x|
                               QPointF( precursor_rect.right(), precursor_rect.top() + 8 ) ]  # a |...x|
                    
                    points.append( points[ 0 ] )
                    
                    painter.drawPolygon( QPolygonF( points ) )
        
        if self.view_model.options.view_names is not False:
            for sequence_view in self.view_model.sequence_views:
                if self.view_model.options.view_names or any(x.isSelected() for x in sequence_view.subsequence_views):
                    leftmost_subsequence = sorted( sequence_view.subsequence_views, key = lambda xx: xx.pos().x() )[ 0 ]
                    text = sequence_view.sequence.accession
                    r = leftmost_subsequence.window_rect()
                    x = r.left() - TEXT_MARGIN - QFontMetrics( painter.font() ).width( text )
                    y = r.top() + r.height() / 2
                    painter.drawText( QPointF( x, y ), text )
    
    
    def __create_components( self ):
        the_list = [ ]
        for s in self.view_model.model.sequences:  # type: LegoSequence
            for ss in s.subsequences:
                self.__connect_components( ss, the_list )
        
        result = [ ]
        
        for set_ in the_list:
            set_2 = [ ]
            result.append( set_2 )
            
            for subsequence in set_:
                set_2.append( self.find_ui_element( subsequence ) )
        
        return result
    
    
    def find_ui_element( self, target: LegoSubsequence ) -> LegoViewSubsequence:
        for sequence_view in self.view_model.sequence_views:
            for subsequence_view in sequence_view.subsequence_views:
                if subsequence_view.subsequence == target:
                    return subsequence_view
        
        raise KeyError( "Cannot find the UI element for the subsequence '{0}'.".format( target ) )
    
    
    @classmethod
    def __connect_components( cls, subsequence: LegoSubsequence, set_list: List[ Set[ LegoViewSubsequence ] ] ):
        for set_ in set_list:
            if subsequence in set_:
                return
        
        set_ = set()
        set_list.append( set_ )
        cls.__connect_to( subsequence, set_ )
    
    
    @classmethod
    def __connect_to( cls, subsequence: LegoSubsequence, target: set ):
        if subsequence in target:
            return  # Already visited
        
        target.add( subsequence )
        
        for edge in subsequence.edges:
            for friend in edge.source + edge.destination:
                cls.__connect_to( friend, target )


class LegoViewModel:
    def __init__( self, focus_notification, model: LegoModel ):
        self.model = model
        self.scene = QGraphicsScene()
        self.sequence_views = [ ]  # type: List[LegoViewSequence]
        self.edges_view = None  # type: Optional[LegoViewAllEdges]
        self.focus_notification=focus_notification
        
        for sequence in self.model.sequences:
            item = LegoViewSequence( self, sequence )
            self.sequence_views.append( item )
        
        self.edges_view = LegoViewAllEdges( self )
        self.scene.addItem( self.edges_view )
        
        self.options = LegoViewOptions()
        
    def selected_subsequence_views ( self )->List[LegoViewSubsequence ]:
        r = []
        
        for x in self.sequence_views:
            for y in x.subsequence_views:
                if y.isSelected():
                    r.append(y)
                    
        return r
    
    
    def update_edges( self ):
        if self.edges_view:
            self.edges_view.update()

    def change_colours( self, new_colour : Union[ QColor, ESequenceColour ], apply_colour:EApply= None ):
            
        if apply_colour is None:
            apply_colour = self.options.colour_apply
        
        the_list = [ ]
        
        if apply_colour == EApply.ALL:
            for x in self.sequence_views:
                the_list.extend( x.subsequence_views )
        elif apply_colour == EApply.EDGES:
            for x in self.sequence_views:
                for y in x.subsequence_views:
                    if y.isSelected():
                        the_list.append( y )
                        the_list.extend( y.edge_subsequence_views )
        elif apply_colour == EApply.ONE:
            for x in self.sequence_views:
                for y in x.subsequence_views:
                    if y.isSelected():
                        the_list.append( y )
        else:
            raise SwitchError("apply_colour", apply_colour)
        
        if isinstance( new_colour, QColor ):
            the_colour = ColourBlock( new_colour )
        
        for subsequence_view in the_list:
            if new_colour == ESequenceColour.RESET:
                the_colour = subsequence_view.component.colour
            elif new_colour == ESequenceColour.RANDOM:
                the_colour = ColourBlock( QColor( randint( 0, 255 ), randint( 0, 255 ), randint( 0, 255 ) ) )
                        
            if self.options.colour_blend != 1:
                subsequence_view.colour = subsequence_view.colour.blend( the_colour.colour, self.options.colour_blend )
            else:
                subsequence_view.colour = the_colour
            
            subsequence_view.update_model()
            subsequence_view.update()


    def add_new_sequence( self, sequence : LegoSequence ):
        view = LegoViewSequence(self, sequence)
        self.sequence_views.append(view)
        self.recreate_edges()
        
    def recreate_sequence(self, sequence:LegoSequence):
        for x in self.sequence_views:
            if x.sequence == sequence:
                x._recreate()
                
        self.recreate_edges()


    def recreate_edges( self ):
        self.scene.removeItem(self.edges_view)
        self.edges_view = LegoViewAllEdges( self )
        self.scene.addItem( self.edges_view )


    def remove_sequence( self, x ):
        pass


COMPONENT_COLOURS = [ QColor( 255, 0, 0 ),  # R
                      QColor( 0, 255, 0 ),  # G
                      QColor( 0, 0, 255 ),  # B
                      QColor( 0, 255, 255 ),  # C
                      QColor( 255, 255, 0 ),  # Y
                      QColor( 255, 0, 255 ),  # M
                      QColor( 0, 255, 128 ),  # Cg
                      QColor( 255, 128, 0 ),  # Yr
                      QColor( 255, 0, 128 ),  # Mr
                      QColor( 0, 128, 255 ),  # Cb
                      QColor( 128, 255, 0 ),  # Yg
                      QColor( 128, 0, 255 ) ]  # Mb ]

KEY_COLOURS = {Qt.Key_0:Colours.BLACK,
               Qt.Key_1:Colours.BLUE,
               Qt.Key_2:Colours.GREEN,
               Qt.Key_3:Colours.CYAN,
               Qt.Key_4:Colours.RED,
               Qt.Key_5:Colours.MAGENTA,
               Qt.Key_6:Colours.YELLOW,
               Qt.Key_7:Colours.WHITE,
               Qt.Key_8:Colours.GRAY,
               Qt.Key_9:Colours.DARK_GRAY,
               Qt.Key_K:Colours.BLACK,
               Qt.Key_B:Colours.BLUE,
               Qt.Key_G:Colours.GREEN,
               Qt.Key_C:Colours.CYAN,
               Qt.Key_R:Colours.RED,
               Qt.Key_M:Colours.MAGENTA,
               Qt.Key_Y:Colours.YELLOW,
               Qt.Key_W:Colours.WHITE,
               Qt.Key_L:Colours.GRAY,
               Qt.Key_D:Colours.DARK_GRAY,
               Qt.Key_P:ESequenceColour.RANDOM,
               Qt.Key_O:ESequenceColour.RESET,
               }