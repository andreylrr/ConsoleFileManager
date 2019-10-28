import filemanager as fm
import bank_account as ba

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
            fm.list_directory("all")
        # Вывести на экран список папок из папки
        elif i_command == 5 :
            fm.list_directory("folder")
        # Вывести на экран список файлов из папки
        elif i_command == 6 :
            fm.list_directory("file")
        # Вывести на экран информацию об операционной системе
        elif i_command == 7 :
            fm.list_os_config()
        # Запустить создателя программ
        elif i_command == 8 :
            fm.program_creator()
        # Запустить викторину
        elif i_command == 9 :
            play_quiz()
        # Запустить приложение "мой счет в банке"
        elif i_command == 10 :
            fm.bank_account()
        # Изменить текущий каталог
        elif i_command == 11 :
            change_current_directory()
        # Выйти из программы
        elif i_command == 12 :
            break


if __name__ == "__main__" :

    console_file_manager()











