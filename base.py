import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtCore
from interface import *

import lista_arquivos
testando = lista_arquivos.testafuncaonova


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.botaoDirA.clicked.connect(self.caminhodirA)

    @QtCore.pyqtSlot()
    def caminhodirA(self):
        #QFileDialog.getOpenFileName(self,"Selecionar Arquivo")
        direotiroA = QFileDialog.getExistingDirectory(self, str("Selecionar Pasta"),"/home",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print("Retorno de Log, Diretorio A lido")
        print("Esté e o caminho lido:", direotiroA)
        return direotiroA


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())