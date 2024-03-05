import os
import shutil

from_dir = ""
to_dir = ""

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:
        path1 = from_dir + '/' + file_name
        path2 = from_dir + '/' + 'arquivos_documentos'
        path3 = from_dir + '/' + 'arquivo_documentos' + file_name

        if os.path.exists(path2):
            print('movendo' + file_name + '....')
            shutil.move(path1, path3)


        else :
            os.makedirs(path2)
            print('movendo' + file_name + '......')
            shutil.move(path1, path3)

