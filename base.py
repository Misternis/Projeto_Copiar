import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import QtCore
from interface import *
import lista_arquivos
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())        #Import maluco do Carlos
original_dir = os.environ.get("original_dir")   #caminho diretorio A
backup_dir = os.environ.get("backup_dir")       #caminho diretorio B


diretorio = lista_arquivos.listarDiretorio(caminho_dir=original_dir)
diretorio = lista_arquivos.listarDiretorio(caminho_dir=backup_dir)


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.botaoDirA.clicked.connect(self.caminhoDirA)
        self.ui.listaDirA.setPlainText(str(lista_arquivos.listarDiretorio))

    @QtCore.pyqtSlot()
    def caminhoDirA(self):
        #QFileDialog.getOpenFileName(self,"Selecionar Arquivo")
        direotiroA = QFileDialog.getExistingDirectory(self, str("Selecionar Pasta"),"/home",QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        print("Retorno de Log, Diretorio 'A' foi lido")
        print("Caminho de diretorio lido:", direotiroA)
        return direotiroA


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())