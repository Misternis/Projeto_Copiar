import os
#import dotenv
#dotenv.load_dotenv(dotenv.find_dotenv())
#
#original_dir = os.environ.get("original_dir")
#backup_dir = os.environ.get("backup_dir")

def listarDiretorio(caminho_dir):
    files = [f for f in os.listdir(caminho_dir) if os.path.isfile(os.path.join(caminho_dir, f))]
    files_count = len(files)
    print(f'Foram listados {files_count} arquivos:')
    for file in files:
        print(file)
    return


#print(listarDiretorio(original_dir))
#print(listarDiretorio(backup_dir))