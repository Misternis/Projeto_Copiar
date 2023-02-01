import os
import shutil
import hashlib
import time

original_dir = 'C:\\Auditor\\AudWhatsApp'
backup_dir = 'C:\\Users\\Suporte\\Desktop\\teste'

# The file extension to backup
backup_extensions = ('.txt', '.dll')

def testafuncaonova():
    files = [f for f in os.listdir(original_dir) if os.path.isfile(os.path.join(original_dir, f))]
    files_count = len(files)
    print(f'Foram listados {files_count} arquivos:')
    for file in files:
        print(file)
    return