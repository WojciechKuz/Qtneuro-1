

from ui_form import Ui_MainWindow
#import knn
import graphmanager as gr

# manage ui signals, trigger actions
class UIManager:
    ui: Ui_MainWindow
    #graphM: gr.GraphManager
    filepoints = []

    def __init__(self, ui: Ui_MainWindow):#, graphM: gr.GraphManager
        self.ui = ui
        # self.graphM = graphM
        # graphM.setOnPressCall(self.startKNN) # when usr sets point, calculate knn

		# receiver functions should be provided
        #self.ui.fileButtonClicked(self.getFile)
        #self.ui.neighbourSpinChanged(self.getNofNeighbours)
        pass

    def __getKNNparams(self):
        """Gets values selected in UI by user.
        
        Returns
        -------
        tuple
			Tuple includes: number of neighbours, metric type, voting system
        """
        ui = self.ui
        #nofNeighbours = ui.neighbourSpin.value()
        return {
            "nofNeighbours" : -5359,
            "metricType" : -6763,
            "votingSys" : -3743
            }

    def startKNN(self, usrpoint: tuple):
        """Calls KNN function"""
        #KNNoutput = knn.knn(self.filepoints, self.__getKNNparams(), usrpoint)
        # self.graphM.drawGraph(KNNoutput[0], usrpoint, KNNoutput[1])
        pass
	
    # reads points and displays it
    def getPoints(self, points): # self or self.ui
        self.filepoints = points
        #print(f"nof rows: {len(self.filepoints)}")
        # self.graphM.loadPoints(self.filepoints)
        # self.graphM.displayPoints()
        pass