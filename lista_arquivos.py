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
    # Use list comprehension to get a list of all files in the directory
    files = [f for f in os.listdir(caminho_dir) if os.path.isfile(os.path.join(caminho_dir, f))]
    
    # Create an empty string
    texto = ''
    
    # Iterate over the files and append their names and modification dates to the string
    for file in files:
        # Get the full path to the file
        file_path = os.path.join(caminho_dir, file)
        
        # Get the modification date of the file
        mod_time = os.path.getmtime(file_path)
        
        # Format the modification date as a string
        mod_time_str = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
        
        # Append the file name and modification date to the string
        texto += f'{file} ({mod_time_str})\n'
    
    # Return the string
    return texto



#print(listarDiretorio(original_dir))
#print(listarDiretorio(backup_dir))