from LabeledTextFile import *

class ConfigurationDialogue(QDialog):

    def __init__(self):
        QDialog.__init__(self)

        self.setWindowTitle("Configuration")
        self.setWindowIcon(QIcon("Logo-Python.png"))

        self.layout = QVBoxLayout()

        self.objet1 = LabeledTextFile("IP address:")
        self.objet2 = LabeledTextFile("User:")
        self.objet3 = LabeledTextFile("Password:")

        self.layout.addWidget(self.objet1)
        self.layout.addWidget(self.objet2)
        self.layout.addWidget(self.objet3)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication([])
    win = ConfigurationDialogue()
    win.show()
    app.exec_()
