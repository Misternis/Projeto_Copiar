# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\viniv\Dropbox\Projetos Dev\Projeto_Copiar\interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(727, 567)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\viniv\\Dropbox\\Projetos Dev\\Projeto_Copiar\\copiar.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textDirA = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textDirA.setFont(font)
        self.textDirA.setObjectName("textDirA")
        self.horizontalLayout.addWidget(self.textDirA)
        self.botaoDirA = QtWidgets.QPushButton(self.centralwidget)
        self.botaoDirA.setObjectName("botaoDirA")
        self.horizontalLayout.addWidget(self.botaoDirA)
        self.caminhoDirA = QtWidgets.QLineEdit(self.centralwidget)
        self.caminhoDirA.setClearButtonEnabled(True)
        self.caminhoDirA.setObjectName("caminhoDirA")
        self.horizontalLayout.addWidget(self.caminhoDirA)
        self.horizontalLayout.setStretch(2, 3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textListaDirA = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textListaDirA.setFont(font)
        self.textListaDirA.setObjectName("textListaDirA")
        self.gridLayout.addWidget(self.textListaDirA, 0, 0, 1, 1)
        self.textListaDirB = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textListaDirB.setFont(font)
        self.textListaDirB.setObjectName("textListaDirB")
        self.gridLayout.addWidget(self.textListaDirB, 0, 1, 1, 1)
        self.tableWidgetA = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetA.setObjectName("tableWidgetA")
        self.tableWidgetA.setColumnCount(3)
        self.tableWidgetA.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetA.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetA.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetA.setHorizontalHeaderItem(2, item)
        self.tableWidgetA.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetA.horizontalHeader().setDefaultSectionSize(113)
        self.gridLayout.addWidget(self.tableWidgetA, 1, 0, 1, 1)
        self.tableWidgetB = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetB.setObjectName("tableWidgetB")
        self.tableWidgetB.setColumnCount(3)
        self.tableWidgetB.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetB.setHorizontalHeaderItem(2, item)
        self.tableWidgetB.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidgetB.horizontalHeader().setDefaultSectionSize(113)
        self.gridLayout.addWidget(self.tableWidgetB, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 727, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Projeto Copiar"))
        self.textDirA.setText(_translate("MainWindow", "Caminho Arquivo:"))
        self.botaoDirA.setText(_translate("MainWindow", "Selecionar"))
        self.caminhoDirA.setAccessibleDescription(_translate("MainWindow", "kjkhjk"))
        self.caminhoDirA.setPlaceholderText(_translate("MainWindow", "Coloque o caminho da pasta aqui."))
        self.textListaDirA.setText(_translate("MainWindow", "DIRETORIO A"))
        self.textListaDirB.setText(_translate("MainWindow", "DIRETORIO B"))
        item = self.tableWidgetA.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidgetA.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidgetA.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tamanho"))
        item = self.tableWidgetB.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nome"))
        item = self.tableWidgetB.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Data"))
        item = self.tableWidgetB.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Tamanho"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
