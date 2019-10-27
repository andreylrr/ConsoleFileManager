import filemanager as fm

"""
    Домашнее задание для 6 урока.
    Реализация консольного файлового менеджера
"""


def print_header():
    print("Выберите пункт меню:")
    print("1  - Создать папку")
    print("2  - Удалить файл/папку")
    print("3  - Копировать файл/папку")
    print("4  - Просмотр содержимого рабочей директории")
    print("5  - Просмотреть только папки")
    print("6  - Просмотреть только файлы")
    print("7  - Просмотр информации об операционной системе")
    print("8  - Создатель программы")
    print("9  - Играть в викторину")
    print("10 - Мой банковский счет")
    print("11 - Смена рабочей директории")
    print("12 - Выход")
    return int(input("Выберите пункт меню :"))

def console_file_manager():

    while True :
        # Вывод меню и обработка пользовательского ввода
        i_command = print_header()

        # В зависимости от того, какой пункт меню был выбран пользователем
        # вызвать соответствующую функцию

        # Создать папку
        if i_command == 1:
            fm.create_folder()
        # Удалить папку
        elif i_command == 2:
            fm.delete_folder()
        # Скопировать папку
        elif i_command == 3:
            fm.copy_folder()
        # Вывести содержимое папки на экран
        elif i_command == 4:
            list_directory()
        # Вывести на экран список папок из папки
        elif i_command == 5 :
            list_only_folders()
        # Вывести на экран список файлов из папки
        elif i_command == 6 :
            list_only_files()
        # Вывести на экран информацию об операционной системе
        elif i_command == 7 :
            list_os_config()
        # Запустить создателя программ
        elif i_command == 8 :
            programm_creater()
        # Запустить викторину
        elif i_command == 9 :
            ply_quiz()
        # Запустить приложение "мой счет в банке"
        elif i_command == 10 :
            my_bank_account
        # Изменить текущий каталог
        elif i_command == 11 :
            change_current_directory()
        # Выйти из программы
        elif i_command == 12 :
            break


if __name__ == "__main__" :

    console_file_manager()











