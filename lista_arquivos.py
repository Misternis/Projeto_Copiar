import os
#import dotenv
#dotenv.load_dotenv(dotenv.find_dotenv())
#
#original_dir = os.environ.get("original_dir")
#backup_dir = os.environ.get("backup_dir")

#def listarDiretorio(caminho_dir):
#    files = [f for f in os.listdir(caminho_dir) if os.path.isfile(os.path.join(caminho_dir, f))]
#    files_count = len(files)
#    print(f'Foram listados {files_count} arquivos:')
#    for file in files:
#        print(file)
#    return

import os
from datetime import datetime

def listarDiretorio(caminho_dir):
    files = [f for f in os.listdir(caminho_dir) if os.path.isfile(os.path.join(caminho_dir, f))]
    texto = ''
    for file in files:
        file_path = os.path.join(caminho_dir, file)
        mod_time = os.path.getmtime(file_path)
        mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        texto += f'{file} ({mod_time_str})\n'
    return texto