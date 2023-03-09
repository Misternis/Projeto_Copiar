import os
import shutil
import hashlib
import time
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

original_dir = os.environ.get("original_dir")
backup_dir = os.environ.get("backup_dir")

ignore_extension = ".ini"
updated_files = 0

for filename in os.listdir(original_dir):
    original_file = os.path.join(original_dir, filename)
    backup_file = os.path.join(backup_dir, filename)

    if os.path.isfile(original_file) and not original_file.endswith(ignore_extension):
        with open(original_file, "rb") as f:
            original_hash = hashlib.md5(f.read()).hexdigest()

        if os.path.isfile(backup_file):
            with open(backup_file, "rb") as f:
                backup_hash = hashlib.md5(f.read()).hexdigest()

            if original_hash != backup_hash:
                shutil.copy2(original_file, backup_file)
                updated_files += 1
        else:
            shutil.copy2(original_file, backup_file)
            updated_files += 1

print(f"{updated_files} arquivos foram atualizados no backup")
