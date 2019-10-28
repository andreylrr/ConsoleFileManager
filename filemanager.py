import os
import shutil as sh
import platform as pl
import pwd

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
    try:
        os.mkdir(create_path(os.getcwd(), s_folder_name))
    except OSError:
        print(f"The folder {s_folder_name} can't be created in {os.getcwd()}")
    else:
        print(f"The folder {s_folder_name} was successfully created in {os.getcwd()}")

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

    if not os._exists(s_old_folder_name):
        print(f"The path: {s_old_folder_name} doesn't exist.")
        return

    if os.path.isfile(s_old_folder_name):
        sh.copyfile(s_old_folder_name, s_new_folder_name)
    else:
        try:
            sh.copytree(s_old_folder_name, s_new_folder_name)
        except OSError as e:
            print(f"Error during coping the folder: {s_old_folder_name} : {e.strerror}")
        print(f"The entered {s_old_folder_name} was copied successfully to {s_new_folder_name}.")

    print(f"The entered: {s_old_folder_name} was copied to: {s_new_folder_name}.")


"""
    Функция вывода содержимого текущего каталога на экран
"""
def list_directory(output_type):
    if output_type == "all":
        map(print, os.listdir(os.getcwd()))
    elif output_type == "file":
        map(print, [x for x in os.listdir((os.getcwd())) if os.path.isfile(x)])
    elif output_type == "folder":
        map(print, [x for x in os.listdir((os.getcwd())) if not os.path.isfile(x)])


def list_config():
    print("Architecture: " + pl.architecture()[0])
    print("Machine: " + pl.machine())
    print("Node: " + pl.node())
    print("Processors: ")
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()
    cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
    for index, item in enumerate(cpuinfo):
        print("    " + str(index) + ": " + item)
    print("System: " + pl.system())
    dist = pl.dist()
    dist = " ".join(x for x in dist)
    print("Distribution: " + dist)
    print("Memory Info: ")
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
    print("     " + lines[0].strip())
    print("     " + lines[1].strip())


def program_creator():
    s_file_name = input("Введите имя файла программы:")
    uid = os.stat(s_file_name).st_uid
    print(f"Создатель программы: {pwd.getpwuid(uid).pw_name}")


def change_current_directory():
    s_path = input("Введите новый рабочий каталог:")
    try:
        os.chdir(s_path)
        print("Рабочий каталог был успешно изменен.")
    except OSError:
        print("Can't change the Current Working Directory")
