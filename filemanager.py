import os
import shutil as sh

"""
    Создание нового пути на основе двух 
"""
def create_path(folder1, folder2):
    if folder1[-1] != "/" and folder2[0] != "/" :
       s_path = folder1 + "/" + folder2
    else:
       s_path = folder1 + folder2
    return s_path

"""
     Функция создания каталога в текущем каталоге
"""
def create_folder():
    s_folder_name = input("Введите название папки:")
    s_current_folder = os.getcwd()
    try:
        os.mkdir(s_current_folder, s_folder_name)
    except OSError:
        print(f"The folder {s_folder_name} can't be created in {s_current_folder}")
    else:
        print(f"The folder {s_folder_name} was successfully created in {s_current_folder}")

def delete_folder():
    s_folder_name = input("Введите название папки:")
    s_current_folder = os.getcwd()
    s_path = create_path(s_current_folder, s_folder_name)

    if not os._exists(s_path):
        print(f"The path: {s_path} doesn't exist in the current folder: {s_current_folder}.")
        return

    if os.path.isfile(s_current_folder+s_folder_name):
        os.remove(s_path)
    else:
        try:
            sh.rmtree(s_path)
        except OSError as e:
            print(f"Error during removing the folder: {s_path} : {e.strerror}")

    print(f"The entered {s_folder_name} was removed successfully.")


 def copy_folder():
    s_old_folder_name = input("Введите название начальной папки/файла:")
    s_new_folder_name = input("Введите название конечной папки/файла:")
    s_current_folder = os.getcwd()

    s_path = create_path(s_current_folder, s_old_folder_name)
    s_path_new = create_path(s_current_folder,s_new_folder_name)
    if not os._exists(s_path):
        print(f"The path: {s_path} doesn't exist in the current folder: {s_current_folder}.")
        return

    if os.path.isfile(s_path):
        sh.copyfile(s_path, s_path_new)
    else:
        try:
            sh.copytree(s_path, s_path_new)
        except OSError as e:
            print(f"Error during moving the folder: {s_path} : {e.strerror}")
        print(f"The entered {s_path} was copied successfully to {s_path_new}.")
    print(f"The entered: {s_old_folder_name} was copied to: {s_new_folder_name}.")

