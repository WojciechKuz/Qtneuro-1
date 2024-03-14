from ui_form import Ui_MainWindow

# manage ui signals, trigger actions
class UIManager:
    ui: Ui_MainWindow

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

		# receiver functions should be provided
        #self.ui.fileButtonClicked(self.getFile)
        #self.ui.neighbourSpinChanged(self.getNofNeighbours)
        pass

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