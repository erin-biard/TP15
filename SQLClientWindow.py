from ButtonsPanel import *
from ConfigurationDialog import *

class SQLClientWindow(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)

        self.layout = QVBoxLayout()

        self.buttonsPanel = ButtonsPanel()
        self.notificationPanel = QTextEdit()
        self.resultTable = QTableWidget()
        self.resultTable.setRowCount(5)
        self.resultTable.setColumnCount(3)
        self.resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout.addWidget(self.buttonsPanel)
        self.layout.addWidget(self.notificationPanel)
        self.layout.addWidget(self.resultTable)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialogue()
   win.show()
   win2 = SQLClientWindow()
   win2.show()
   app.exec_()
