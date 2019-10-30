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
        print(f"Папка: {s_folder_name} не может быть создана в {os.getcwd()}")
    else:
        print(f"Папка: {s_folder_name} создана в {os.getcwd()}")



"""
    Функция удаления каталога
"""
def delete_folder():
    s_folder_name = input("Введите название папки:")
    s_current_folder = os.getcwd()
    s_path = create_path(s_current_folder, s_folder_name)

    if not os.path.exists(s_path):
        print(f"Папка: {s_folder_name} не существует в текущем каталоге: {s_current_folder}.")
        return

    if os.path.isfile(s_current_folder+s_folder_name):
        os.remove(s_path)
    else:
        try:
            sh.rmtree(s_path)
        except OSError as e:
            print(f"Возникла ошиька при копировании папки: {s_path} : {e.strerror}")

    print(f"Папка: {s_folder_name} была успешно удалена.")


"""
    Функция копирования каталога/файла
"""
def copy_folder():
    s_old_folder_name = input("Введите название начальной папки/файла:")
    s_new_folder_name = input("Введите название конечной папки/файла:")

    if not os.path.exists(s_old_folder_name):
        print(f"Путь: {s_old_folder_name} не существует.")
        return

    if os.path.isfile(s_old_folder_name):
        sh.copyfile(s_old_folder_name, s_new_folder_name)
        print(f"Файл: {s_old_folder_name} успшено скопирован в: {s_new_folder_name}.")
    else:
        try:
            sh.copytree(s_old_folder_name, s_new_folder_name)
        except OSError as e:
            print(f"Возникла ошибка при копировании папки: {s_old_folder_name} : {e.strerror}")
        print(f"Каталог/файл : {s_old_folder_name} был скопирован успешно в: {s_new_folder_name}.")


"""
    Функция вывода содержимого текущего каталога на экран
"""
def list_directory(output_type):
    if output_type == "all":
        print(os.listdir(os.getcwd()))
    elif output_type == "file":
        print([x for x in os.listdir((os.getcwd())) if os.path.isfile(x)])
    elif output_type == "folder":
        print([x for x in os.listdir((os.getcwd())) if not os.path.isfile(x)])


"""
    Функция выода информации о системе
"""
def list_config():
    print("Архитектура: " + pl.architecture()[0])
    print("Машина: " + pl.machine())
    print("Узел: " + pl.node())
    print("Процессоры: ")
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()
    cpuinfo = [x.strip().split(":")[1] for x in info if "model name" in x]
    for index, item in enumerate(cpuinfo):
        print("    " + str(index) + ": " + item)
    print("Система: " + pl.system())
    dist = pl.dist()
    dist = " ".join(x for x in dist)
    print("Дистрибуция: " + dist)
    print("Память: ")
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
    print("     " + lines[0].strip())
    print("     " + lines[1].strip())


"""
    Функция вывода имени создателя файла
"""
def program_creator():
    s_file_name = input("Введите имя файла программы:")
    uid = os.stat(s_file_name).st_uid
    print(f"Создатель программы: {pwd.getpwuid(uid).pw_name}")



"""
    Функция изменения текущего рабочего каталога
"""
def change_current_directory():
    s_path = input("Введите новый рабочий каталог:")
    try:
        os.chdir(s_path)
        print("Рабочий каталог был успешно изменен.")
    except OSError:
        print("Текущий рабочий каталог не может быть изменен.")
