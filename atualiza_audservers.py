import shutil
import os

def atualiza_audservers(diretorio_origem, diretorio_destino, nomes_arquivos):
    for nome_arquivo in nomes_arquivos:
        origem = os.path.join(diretorio_origem, nome_arquivo)
        destino = os.path.join(diretorio_destino, nome_arquivo)
        shutil.copy(origem, destino)

# Exemplo de uso:
diretorio_origem = '//newton/PrgAuditorWin/VsCompilada'
diretorio_destino = 'C:/Auditor/Programas'
nomes_arquivos = ['audservers.dll', 'Audlibcli.cfg']  # Lista de nomes de arquivos que você deseja copiar

atualiza_audservers(diretorio_origem, diretorio_destino, nomes_arquivos)
