from PySide2.QtWidgets import *
from PySide2.QtGui import *

class LabeledTextFile(QWidget):

    def __init__(self,text):
        QWidget.__init__(self)
        self.__text = text

        self.layout = QHBoxLayout()

        self.text = QLabel(text)
        self.textEdit = QTextEdit()
        self.textEdit.setMaximumHeight(23)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.textEdit)

        self.setLayout(self.layout)
