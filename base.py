import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidget, QTableWidgetItem
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
        #self.ui.tableWidgetA.setPlainText(str(lista_arquivos.listarDiretorio(caminho_dir=original_dir)))               # Adiciona a String na lista A
        #self.ui.tableWidgetA.addItem(str(lista_arquivos.listarDiretorio(caminho_dir=original_dir)))                   # Adiciona a String na lista B    
        lista = ['Carro', 'Vinicios', 'Bumbum de Nenem', 'igoroi']
        self.ui.tableWidgetA.setRowCount(len(lista))
        for i in lista:
            item_name = QTableWidgetItem(i)
            item_data = QTableWidgetItem('data')
            item_tamanho = QTableWidgetItem('tamanho')
            self.ui.tableWidgetA.setItem(lista.index(i),0,item_name)
            self.ui.tableWidgetA.setItem(lista.index(i),1,item_data)
            self.ui.tableWidgetA.setItem(lista.index(i),2,item_tamanho)
        #result = {'nome':['Vinicios'], 'data': ['05/06/1994'], 'tamanho':['igoroi']}
        #self.ui.tableWidgetA.clearContents()
        #self.ui.tableWidgetA.setRowCount(len(result))
        #for row, text in enumerate(result):
        #    for column, data in enumerate(text):
        #        self.ui.tableWidgetA.setItem(row, column, QTableWidgetItem(str(data)))

            

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