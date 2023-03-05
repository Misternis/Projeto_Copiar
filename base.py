import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTableWidget, QTableWidgetItem
from PyQt5 import QtCore
from interface import *
import lista_arquivos
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv()) 
original_dir = os.environ.get("original_dir")   #caminho diretorio A
backup_dir = os.environ.get("backup_dir")       #caminho diretorio B


diretorioA = lista_arquivos.listarDiretorio(caminho_dir=original_dir)
diretorioB = lista_arquivos.listarDiretorio(caminho_dir=backup_dir)


class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.botaoDirA.clicked.connect(self.caminhoDirA)        
        self.ui.tableWidgetA.setRowCount(len(diretorioA))
        self.ui.tableWidgetB.setRowCount(len(diretorioB))
        
        for i in diretorioA:    #Adiciona items a lista no TableWidgetA
            item_name = QTableWidgetItem(i['name'])
            item_data = QTableWidgetItem(i['date'])
            item_tamanho = QTableWidgetItem(i['size'])
            self.ui.tableWidgetA.setItem(diretorioA.index(i),0,item_name)
            self.ui.tableWidgetA.setItem(diretorioA.index(i),1,item_data)
            self.ui.tableWidgetA.setItem(diretorioA.index(i),2,item_tamanho)

        for i in diretorioB:    #Adiciona items a lista no TableWidgetB
            item_name = QTableWidgetItem(i['name'])
            item_data = QTableWidgetItem(i['date'])
            item_tamanho = QTableWidgetItem(i['size'])
            self.ui.tableWidgetB.setItem(diretorioB.index(i),0,item_name)
            self.ui.tableWidgetB.setItem(diretorioB.index(i),1,item_data)
            self.ui.tableWidgetB.setItem(diretorioB.index(i),2,item_tamanho)
            

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