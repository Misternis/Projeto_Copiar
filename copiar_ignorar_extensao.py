import os
import shutil
import hashlib
import time

original_dir = 'C:\\siAuditor\\AudWhatsApp'
backup_dir = 'C:\\Users\\Suporte\\Desktop\\teste'

# The file extension to ignore
ignore_extension = '.ini'

files_count = len([f for f in os.listdir(original_dir) if os.path.isfile(os.path.join(original_dir, f))])
print(f'Foram listados {files_count} arquivos')
answer = input("Deseja continuar? (SIM/NAO)")
if answer.upper() == "SIM":
    for filename in os.listdir(original_dir):
        original_file = os.path.join(original_dir, filename)
        backup_file = os.path.join(backup_dir, filename)
        if os.path.isfile(original_file):
            # Check if the file extension matches the extension to ignore
            if not original_file.endswith(ignore_extension):
                # Calculate the hash of the file in the original directory
                original_hash = hashlib.md5()
                print(f'Verificando Hash do arquivo original: {filename}')
                with open(original_file, 'rb') as f:
                    original_hash.update(f.read())
                original_hash = original_hash.hexdigest()

                # Check if the file exists in the backup directory
                if os.path.isfile(backup_file):
                    # Calculate the hash of the file in the backup directory
                    backup_hash = hashlib.md5()
                    print(f'Verificando Hash do arquivo em Backup: {filename}')
                    with open(backup_file, 'rb') as f:
                        backup_hash.update(f.read())
                    backup_hash = backup_hash.hexdigest()

                    # Compare the hash of the file in the original directory and the backup directory
                    if original_hash != backup_hash:
                        # If the file in the original directory is different, copy it to the backup directory
                        shutil.copy2(original_file, backup_file)
                        print(f'Arquivo {filename} foi atualizado e foi feito Backup')
                    else:
                        print(f'Arquivo {filename} não foi atualizado')
                else:
                    shutil.copy2(original_file, backup_file)
                    print(f'Arquivo {filename} foi feito Backup')
        time.sleep(5)