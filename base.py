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

        ##self.ui.centralwidget.
        

    #def diretorioA(self):
    #    pass
    #    QFileDialog.getOpenFileName(self,"Abrir Pasta")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())