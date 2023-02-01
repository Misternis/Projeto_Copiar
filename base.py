import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore
from interface import *

import lista_arquivos
testando = lista_arquivos.testafuncaonova

class Sinais(QtCore.QObject):
    sinal1 = QtCore.pyqtSignal()


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sinais = Sinais()
        self.ui.pushButtonNovo.clicked.connect(self.funcao1)
        
    
    @QtCore.pyqtSlot()
    def funcao1(self):
        print("Botão Foi Clicado")
        print(testando())
        self.sinais.sinal1.connect(self.recebeSinal)
        self.sinais.sinal1.emit()
        self.sinais.sinal1.disconnect()


    def recebeSinal(self):
        print("Sinal Recebido com Sucesso.")

    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())