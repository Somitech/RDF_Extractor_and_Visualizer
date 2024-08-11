from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.urlInput = QtWidgets.QLineEdit(self.centralwidget)
        self.urlInput.setObjectName("urlInput")
        self.verticalLayout.addWidget(self.urlInput)

        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setObjectName("extractButton")
        self.extractButton.setText("Extract Data")
        self.verticalLayout.addWidget(self.extractButton)

        self.rdfOutput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.rdfOutput.setObjectName("rdfOutput")
        self.verticalLayout.addWidget(self.rdfOutput)

        self.visualizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.visualizeButton.setObjectName("visualizeButton")
        self.visualizeButton.setText("Visualize RDF Graph")
        self.verticalLayout.addWidget(self.visualizeButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))