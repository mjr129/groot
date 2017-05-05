from random import randint
from typing import List, Optional

from PyQt5.QtCore import QCoreApplication, QRectF, Qt, pyqtSlot
from PyQt5.QtGui import QColor, QStandardItemModel, QStandardItem
from PyQt5.QtOpenGL import QGL, QGLFormat, QGLWidget
from PyQt5.QtWidgets import QColorDialog, QFileDialog, QGraphicsScene, QMainWindow, QMessageBox, QInputDialog

from Designer.FrmMain_designer import Ui_MainWindow
from LegoModels import LegoEdge, LegoModel, LegoSequence, LegoSubsequence
from LegoViews import EApply, ESequenceColour, LegoViewModel, LegoViewSubsequence
from MHelper import IoHelper, QtGuiHelper
from MHelper.QtColourHelper import Colours


class FrmMain( QMainWindow ):
    """
    Main window
    """
    
    
    def __init__( self ) -> None:
        """
        CONSTRUCTOR
        """
        self.no_update_options = False
        
        QCoreApplication.setAttribute( Qt.AA_DontUseNativeMenuBar )
        
        # QT stuff
        QMainWindow.__init__( self )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )
        self.setWindowTitle( "Lego Model Creator" )
        
        # Open GL rendering
        self.ui.graphicsView.setViewport( QGLWidget( QGLFormat( QGL.SampleBuffers ) ) )
        
        # Default (empty) scene
        scene = QGraphicsScene()
        scene.addRect( QRectF( -10, -10, 20, 20 ) )
        self.ui.graphicsView.setInteractive( True )
        self.ui.graphicsView.setScene( scene )
        
        # Load our sample model
        self._model = LegoModel()
        # self._model.read_blast("./SampleData/blast.blast")
        self._model.import_composites( "/Users/martinrusilowicz/HiddenDesktop/COMPOSITES/A0A024WP05.composites" )
        
        self._view = None  # type:LegoViewModel
        self.refresh_model()
        
        self.statusBar().showMessage( "LMB = Select | LMB+Drag = Move sequence; Shift = Move subsequence; Ctrl = No X-snap; Alt = No Y-snap | 0-9 RGB CYMK W = Change colour; Shift = Bright colour; Ctrl = Recursive | X = Restore all colours", 0 )
    
    
    def subsequence_view_focus( self, subsequence_view: LegoViewSubsequence ):
        ss = subsequence_view.subsequence
        self.ui.LST_SEQUENCES.setCurrentIndex( self._model.sequences.index( ss.sequence ) )
        self.ui.LST_SUBSEQUENCES.setCurrentIndex( ss.sequence.subsequences.index( ss ) )
    
    
    def refresh_model( self ):
        self.no_update_options = True
        self._view = LegoViewModel( self.subsequence_view_focus, self._model )
        self.ui.graphicsView.setScene( self._view.scene )
        
        self.ui.LST_SEQUENCES.clear()
        self.ui.LST_SEQUENCES.addItems( x.accession for x in self._model.sequences )
        
        o = self._view.options
        self.ui.CHK_MOVE_XSNAP.setChecked( o.x_snap )
        self.ui.CHK_MOVE_YSNAP.setChecked( o.y_snap )
        self.ui.RAD_COL_CONNECTED.setChecked( o.colour_apply == EApply.EDGES )
        self.ui.RAD_COL_ALL.setChecked( o.colour_apply == EApply.ALL )
        self.ui.RAD_COL_SELECTION.setChecked( o.colour_apply == EApply.ONE )
        self.ui.CHK_COL_BLEND.setChecked( o.colour_blend != 1 )
        self.ui.SLI_BLEND.setValue( o.colour_blend * 100 )
        self.ui.SLI_BLEND.setVisible( self.ui.CHK_COL_BLEND.isChecked() )
        self.ui.CHK_VIEW_EDGES.setCheckState( QtGuiHelper.to_check_state( o.view_edges ) )
        self.ui.CHK_VIEW_NAMES.setCheckState( QtGuiHelper.to_check_state( o.view_names ) )
        self.ui.CHK_VIEW_PIANO_ROLLS.setCheckState( QtGuiHelper.to_check_state( o.view_piano_roll ) )
        self.ui.CHK_VIEW_POSITIONS.setCheckState( QtGuiHelper.to_check_state( o.view_positions ) )
        
        self.no_update_options = False
    
    
    def closeEvent( self, *args, **kwargs ):
        """
        OVERRIDE
        Fixes crash on exit on Windows
        """
        exit()
    
    
    def update_options( self ):
        if self.no_update_options:
            return
        
        o = self._view.options
        o.x_snap = self.ui.CHK_MOVE_XSNAP.isChecked()
        o.y_snap = self.ui.CHK_MOVE_YSNAP.isChecked()
        o.colour_apply = EApply.EDGES if self.ui.RAD_COL_CONNECTED.isChecked() \
            else EApply.ALL if self.ui.RAD_COL_ALL.isChecked() \
            else EApply.ONE if self.ui.RAD_COL_SELECTION.isChecked() else None
        o.colour_blend = self.ui.SLI_BLEND.value() / 100 if self.ui.CHK_COL_BLEND.isChecked() else 1
        o.view_edges = QtGuiHelper.from_check_state( self.ui.CHK_VIEW_EDGES.checkState() )
        o.view_names = QtGuiHelper.from_check_state( self.ui.CHK_VIEW_NAMES.checkState() )
        o.view_piano_roll = QtGuiHelper.from_check_state( self.ui.CHK_VIEW_PIANO_ROLLS.checkState() )
        o.view_positions = QtGuiHelper.from_check_state( self.ui.CHK_VIEW_POSITIONS.checkState() )
        
        self.ui.SLI_BLEND.setVisible( self.ui.CHK_COL_BLEND.isChecked() )
        
        self._view.scene.update()
        
        self.statusBar().showMessage( str( randint( 0, 1000 ) ), 0 )
    
    
    @pyqtSlot( int )
    def on_CHK_VIEW_EDGES_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_VIEW_NAMES_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_VIEW_PIANO_ROLLS_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_VIEW_POSITIONS_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_MOVE_XSNAP_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_MOVE_YSNAP_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_CHK_COL_BLEND_stateChanged( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( bool )
    def on_RAD_COL_CONNECTED_toggled( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( bool )
    def on_RAD_COL_SELECTION_toggled( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( bool )
    def on_RAD_COL_ALL_toggled( self, _ ):
        self.update_options()
    
    
    @pyqtSlot( int )
    def on_SLI_BLEND_valueChanged( self, _ ):
        self.update_options()
    
    
    def apply_colour( self, new_colour, darken = True ):
        if darken and self.ui.BTNCHK_DARKER.isChecked():
            new_colour = QColor( new_colour.red() // 2, new_colour.green() // 2, new_colour.blue() // 2 )
        
        self._view.change_colours( new_colour )
    
    
    @pyqtSlot( int )
    def on_LST_SEQUENCES_currentIndexChanged( self, _ ):
        self.ui.LST_SUBSEQUENCES.clear()
        
        seq = self.listbox_sequence()
        
        if seq:
            self.ui.LST_SUBSEQUENCES.addItems(seq.subsequences)
    
    
    def listbox_sequence( self ) -> LegoSequence:
        return self._model.sequences[ self.ui.LST_SEQUENCES.currentIndex() ] if self.ui.LST_SEQUENCES.currentIndex() != -1 else None
    
    def selected_subsequences(self)->List[LegoSubsequence]:
        return [x.subsequence for x in self._view.selected_subsequence_views()]
    
    def selected_sequences(self)->List[LegoSequence]:
        return list(set(x.subsequence.sequence for x in self._view.selected_subsequence_views()))
    
    def selected_sequence(self)->Optional[LegoSequence]:
        sequences = self.selected_sequences()
        
        if len(sequences)!=1:
            return None
        
        return sequences[0]
    
    
    def listbox_subsequence( self ) -> LegoSubsequence:
        s = self.listbox_sequence()
        
        return s.subsequences[ self.ui.LST_SUBSEQUENCES.currentIndex() ] if self.ui.LST_SUBSEQUENCES.currentIndex() != -1 else None
    
    
    def listbox_edge( self ) -> LegoEdge:
        ss = self.listbox_subsequence()
        
        return ss.edges[ self.ui.LST_EDGES.currentIndex() ] if self.ui.LST_EDGES.currentIndex() != -1 else None
    
    
    @pyqtSlot( int )
    def on_LST_SUBSEQUENCES_currentIndexChanged( self, _ ):
        self.ui.LST_EDGES.clear()
        
        sseq = self.listbox_subsequence()
        
        if sseq:
            for edge in sseq.edges:
                self.ui.LST_EDGES.addItems( "--> {0} ({1} - {2})".format( x.sequence.accession, x.start, x.end ) for x in edge.source )
                self.ui.LST_EDGES.addItems( "<-- {0} ({1} - {2})".format( x.sequence.accession, x.start, x.end ) for x in edge.destination )
    
    
    @pyqtSlot()
    def on_BTNCHK_DARKER_clicked( self ) -> None:
        """
        Signal handler: Darker check-button clicked
        """
        self.ui.ACTCHK_DARKER.setChecked( self.ui.BTNCHK_DARKER.isChecked() )
    
    
    @pyqtSlot()
    def on_BTN_BLANK_clicked( self ) -> None:
        """
        Signal handler: Blanking plate clicked
        """
        pass  # nothing to do
    
    
    @pyqtSlot()
    def on_ACT_MODEL_NEW_triggered( self ) -> None:
        """
        Signal handler: New model
        """
        self._model = LegoModel()
        self.refresh_model()
    
    
    @pyqtSlot()
    def on_ACT_MODEL_IMPORT_triggered( self ) -> None:
        """
        Signal handler: Import data
        """
        filters = "FASTA files (*.fasta *.fa)", "BLAST output (*.blast *.tsv)", "Composite finder output (*.composites)"
        
        file_name, filter = QFileDialog.getOpenFileName( self, "Select file", None, ";;".join( filters ) )
        
        if not file_name:
            return
        
        filter_index = filters.index( filter )
        
        if filter_index == 0:
            self._model.read_fasta( file_name )
        elif filter_index == 1:
            self._model.import_blast( file_name )
        elif filter_index == 2:
            self._model.import_composites( file_name )
        
        self.refresh_model()
    
    
    @pyqtSlot()
    def on_ACT_APP_EXIT_triggered( self ) -> None:
        """
        Signal handler: Exit application
        """
        self.close()
    
    
    @pyqtSlot()
    def on_ACT_MODEL_SAVE_triggered( self ) -> None:
        """
        Signal handler: Save model
        """
        file_name = QtGuiHelper.browse_save( self, "Genetic lego (*.glego)" )
        
        if file_name:
            IoHelper.save_binary( file_name, self._model )
    
    
    @pyqtSlot()
    def on_ACT_MODEL_OPEN_triggered( self ) -> None:
        """
        Signal handler:
        """
        file_name = QtGuiHelper.browse_open( self, "Genetic lego (*.glego)" )
        
        if file_name:
            try:
                self._model = IoHelper.load_binary( file_name )
                self.refresh_model()
            except Exception as ex:
                QtGuiHelper.show_exception( self, "Could not load the file. Perhaps it is from a different version?", ex )
    
    
    @pyqtSlot()
    def on_ACT_MODEL_QUANTISE_triggered( self ) -> None:
        """
        Signal handler:
        """
        level, ok = QInputDialog.getInt(self, self.windowTitle(), "This option will quantise subsequence positions to the nearest 'n', where 'n' is:", 10, 2, 1000)
        
        if not ok:
            return
        
        self._model.quantise(level)
    
    
    @pyqtSlot()
    def on_ACT_NEW_SEQUENCE_triggered( self ) -> None:
        """
        Signal handler:
        """
        sequence = self._model.add_new_sequence()
        self._view.add_new_sequence(sequence)
    
    
    @pyqtSlot()
    def on_ACT_NEW_EDGE_triggered( self ) -> None:
        """
        Signal handler:
        """
        subsequences = self.selected_subsequences()
    
        try:
            self._model.add_new_edge(subsequences)
            self._view.recreate_edges()
            
        except Exception as ex:
            QtGuiHelper.show_exception(self, ex)
        
    
    
    @pyqtSlot()
    def on_ACT_NEW_SPLIT_triggered( self ) -> None:
        """
        Signal handler:
        """
        subsequences = self.selected_subsequences()
        sequence = self.selected_sequence()
        
        if not sequence:
            return
        
        default_split = (min(x.start for x in subsequences) + max(x.end for x in subsequences)) // 2
        split_point, ok = QInputDialog.getInt(self, self.windowTitle(), "Split the sequence '{0}' into [1:x] and [x+1:n] where x = ",default_split, 1, sequence.length )
        
        if not ok:
            return 
        
        try:
            self._model.add_new_subsequence(sequence, split_point)
            self._view.recreate_sequence(sequence)
        
        except Exception as ex:
            QtGuiHelper.show_exception(self, ex)
    
    @pyqtSlot()
    def on_ACT_REMOVE_SEQUENCE_triggered( self ) -> None:
        """
        Signal handler:
        """
        sequences = self.selected_subsequences()
        
        for x in sequences:
            self._model.remove_sequence(x)
            self._view.remove_sequence(x)
    
    
    @pyqtSlot()
    def on_ACT_REMOVE_EDGE_triggered( self ) -> None:
        """
        Signal handler:
        """
        QMessageBox.information( self, "todo", "on_ACT_REMOVE_EDGE_triggered" )
    
    
    @pyqtSlot()
    def on_ACT_REMOVE_SPLIT_triggered( self ) -> None:
        """
        Signal handler:
        """
        QMessageBox.information( self, "todo", "on_ACT_REMOVE_SPLIT_triggered" )
    
    
    @pyqtSlot()
    def on_ACT_COL_RED_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.RED )
    
    
    @pyqtSlot()
    def on_ACT_COL_GREEN_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.GREEN )
    
    
    @pyqtSlot()
    def on_ACT_COL_BLUE_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.BLUE )
    
    
    @pyqtSlot()
    def on_ACT_COL_CYAN_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.CYAN )
    
    
    @pyqtSlot()
    def on_ACT_COL_MAGENTA_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.MAGENTA )
    
    
    @pyqtSlot()
    def on_ACT_COL_YELLOW_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.YELLOW )
    
    
    @pyqtSlot()
    def on_ACT_COL_BLACK_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.BLACK )
    
    
    @pyqtSlot()
    def on_ACT_COL_GRAY_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.GRAY )
    
    
    @pyqtSlot()
    def on_ACT_COL_WHITE_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( Colours.WHITE )
    
    
    @pyqtSlot()
    def on_ACT_WINDOW_COLOURS_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.ui.DOCK_COLOURS.setVisible( self.ui.ACT_WINDOW_COLOURS.isChecked() )
    
    
    @pyqtSlot( bool )
    def on_DOCK_COLOURS_visibilityChanged( self, visible ):
        self.ui.ACT_WINDOW_COLOURS.setChecked( visible )
    
    
    @pyqtSlot()
    def on_ACT_COL_RESET_triggered( self ) -> None:
        """
        Signal handler:
        """
        self.apply_colour( ESequenceColour.RESET, False )
    
    
    @pyqtSlot()
    def on_ACT_COL_CUSTOM_triggered( self ) -> None:
        """
        Signal handler:
        """
        new_colour = QColorDialog.getColor( Qt.white, self )
        
        if new_colour is not None:
            self.apply_colour( new_colour, False )
    
    
    @pyqtSlot()
    def on_ACT_DETAILS_SEQUENCE_triggered( self ) -> None:
        """
        Signal handler:
        """
        s = self.listbox_sequence()
        
        details = [ ]
        details.append( "accession = {}".format( s.accession ) )
        details.append( "subsequences = {}".format( s.subsequences ) )
        details.append( "length = {}".format( s.length ) )
        details.append( "array = {}".format( s.array ) )
        details.append( "meta = {}".format( s.meta ) )
        
        b = QMessageBox()
        b.setText( str( s ) )
        b.setInformativeText( "\n".join( details ) )
        b.exec_()
    
    
    @pyqtSlot()
    def on_ACT_DETAILS_EDGE_triggered( self ) -> None:
        """
        Signal handler:
        """
        s = self.listbox_edge()
        
        details = [ ]
        details.append( "source = {}[{}:{}]".format( s.source_sequence, s.source_start, s.source_end ) )
        details.append( "destination = {}[{}:{}]".format( s.destination_sequence, s.destination_start, s.destination_end ) )
        details.append( "sources = {}".format( s.source ) )
        details.append( "destinations = {}".format( s.destination ) )
        
        b = QMessageBox()
        b.setText( str( s ) )
        b.setInformativeText( "\n".join( details ) )
        b.exec_()
    
    
    @pyqtSlot()
    def on_ACT_DETAILS_SPLIT_triggered( self ) -> None:
        """
        Signal handler:
        """
        s = self.listbox_subsequence()
        
        details = [ ]
        details.append( "sequence = {}".format( s.sequence.accession ) )
        details.append( "start = {}".format( s.start ) )
        details.append( "end = {}".format( s.end ) )
        details.append( "edges = {}".format( s.edges ) )
        details.append( "ui position = {}".format( s.ui_position ) )
        details.append( "ui colour = {}".format( s.ui_colour ) )
        details.append( "array = {}".format( s.array ) )
        
        b = QMessageBox()
        b.setText( str( s ) )
        b.setInformativeText( "\n".join( details ) )
        b.exec_()
    
    
    @pyqtSlot()
    def on_ACTCHK_DARKER_triggered( self ) -> None:
        """
        Signal handler: "Darker" check-button
        """
        self.ui.BTNCHK_DARKER.setChecked( self.ui.ACTCHK_DARKER.isChecked() )
    
    
    @pyqtSlot()
    def on_ACT_COL_DARK_GRAY_triggered( self ) -> None:
        """
        Signal handler: Colour dark gray
        """
        self.apply_colour( Colours.DARK_GRAY, False )
    
    
    @pyqtSlot()
    def on_ACT_REMOVE_SELECTION_triggered( self ) -> None:
        """
        Signal handler:
        """
        pass
    
    
    @pyqtSlot()
    def on_ACT_DETAILS_SELECTION_triggered( self ) -> None:
        """
        Signal handler:
        """
        pass
    
    
    @pyqtSlot()
    def on_ACT_COL_RANDOM_triggered( self ) -> None:
        """
        Signal handler: Random colour
        """
        self.apply_colour( ESequenceColour.RANDOM, False )
