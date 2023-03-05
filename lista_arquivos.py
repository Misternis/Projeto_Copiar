import os
from datetime import datetime

def listarDiretorio(caminho_dir):
    files = [f for f in os.listdir(caminho_dir) if os.path.isfile(os.path.join(caminho_dir, f))] # Obtém uma lista de arquivos no diretório especificado em "caminho_dir". Em seguida, cria uma nova lista "files" que contém apenas os arquivos (e não diretórios).
    dados = []
    for file in files:
        file_path = os.path.join(caminho_dir, file)     # Caminho do Arquivo (Path)
        mod_time = os.path.getmtime(file_path)          # Data do arquivo
        mod_size = os.path.getsize(file_path) / 1000    # Tamanho do Arquivo em Kbts
        mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')      # Data Arquivo e converte em String
        dados.append({'name': file, 'date': mod_time_str, 'size': ("%.2f" % mod_size + " Kbts").replace('.',',')})      # Adicionar o Dic com as info a lista 'Dados'
    return dados