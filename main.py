import os, tempfile
from pyzipper import AESZipFile
from rarfile import RarFile
from py7zr import SevenZipFile

MAX_PASS_LENGTH = 6  # Можно менять на 7, 8, но время резко возрастает

def findArchive():
    archive_extensions = ('.zip', '.rar', '.7z')
    for file in os.listdir():
        if file.lower().endswith(archive_extensions):
            return file
    raise FileNotFoundError("Архив (ZIP/RAR/7Z) не найден в текущей папке")

def openArchive(filename):
    if filename.lower().endswith('.zip'):
        return AESZipFile(filename)
    elif filename.lower().endswith('.rar'):
        return RarFile(filename)
    elif filename.lower().endswith('.7z'):
        return SevenZipFile(filename)
    raise ValueError("Неизвестный формат архива")

def genNumPass(passLen = MAX_PASS_LENGTH):
    for length in range(1, passLen + 1):
        for i in range(10**length):
            yield f"{i:0{length}d}"

archive_path = findArchive()

if archive_path.lower().endswith('.zip'):
    archive = openArchive(archive_path)
    for password in genNumPass():
        try:
            archive.extractall(pwd=password.encode())
            print(f"Пароль найден: {password}")
            break
        except Exception: continue
    archive.close()
elif archive_path.lower().endswith('.rar'):
    archive = openArchive(archive_path)
    for password in genNumPass():
        try:
            archive.extractall(pwd=password)
            print(f"Пароль найден: {password}")
            break
        except Exception: continue
    archive.close()
elif archive_path.lower().endswith('.7z'):
    for password in genNumPass():
        try:
            with tempfile.TemporaryDirectory() as tmpdirname:
                with SevenZipFile(archive_path, mode='r', password=password) as archive:
                    archive.extractall(path=tmpdirname)
                print(f"Пароль найден: {password}")
                break
        except Exception: continue
