import os
import shutil as sh

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

    if s_current_folder[-1] != "/" and s_folder_name[0] != "/" :
       s_path = s_current_folder + "/" + s_folder_name
    else:
       s_path = s_current_folder + s_folder_name

    if not os._exists(s_path):
        print(f"The path {s_path} doesn't exist in the current folder {s_current_folder}.")
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

    



    try:
        sh.rmtree()
