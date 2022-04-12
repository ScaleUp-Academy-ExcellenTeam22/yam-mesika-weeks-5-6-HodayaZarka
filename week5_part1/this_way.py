import os

path = input("Please Enter directory path: ")
all_files = os.listdir(path)
print(all_files)
files = [file for file in all_files if file.startswith("deep")]
print(files)

