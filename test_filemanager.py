import bank_account as ba
import filemanager as fm
import os
import json

"""
   Тесты для функции refill из программы bank_account
"""
def test_refill_account(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "50")
    test_account = 0
    l_test_history = []
    result = ba.refill(test_account, l_test_history)
    assert result[1][0] == "Счет пополнен на 50 рублей."
    assert result[0] == 50

def test_refill_account_multiple_entries(monkeypatch):
    test_account = 0
    l_test_history = []
    monkeypatch.setattr('builtins.input', lambda x: "50")
    test_account, l_test_history = ba.refill(test_account, l_test_history)
    monkeypatch.setattr('builtins.input', lambda x: "150")
    test_account, l_test_history = ba.refill(test_account, l_test_history)
    monkeypatch.setattr('builtins.input', lambda x: "-20")
    test_account, l_test_history = ba.refill(test_account, l_test_history)
    assert test_account == 180
    assert l_test_history[0] == "Счет пополнен на 50 рублей."
    assert l_test_history[1] == "Счет пополнен на 150 рублей."
    assert l_test_history[2] == "Счет пополнен на -20 рублей."


"""
    Тесты для функции purchase
"""
def test_purchase(monkeypatch):
    test_account = 200
    l_test_history = []
    l_input_data = ["50", "Обувь"]
    monkeypatch.setattr('builtins.input', lambda x: l_input_data.pop(0))
    test_account, l_test_history = ba.purchase(test_account, l_test_history)
    assert test_account == 150
    assert l_test_history[0] == f"Совершена покупка \"Обувь\" на сумму 50."

def test_purchase_multiple(monkeypatch):
    l_test_print = []
    test_account = 200
    l_test_history = []

    def add_print(x):
        l_test_print.append(x)

    l_input_data = ["50", "Обувь"]
    monkeypatch.setattr('builtins.input', lambda x: l_input_data.pop(0))
    monkeypatch.setattr('builtins.print', add_print)
    test_account, l_test_history = ba.purchase(test_account, l_test_history)
    l_input_data = ["50", "Куртка"]
    test_account, l_test_history = ba.purchase(test_account, l_test_history)
    assert l_test_print[0] == "Покупка успешно совершена. На счету осталось 150."
    assert test_account == 100
    assert l_test_history[0] == f"Совершена покупка \"Обувь\" на сумму 50."
    assert l_test_history[1] == f"Совершена покупка \"Куртка\" на сумму 50."

def test_purchase_negative(monkeypatch):
    l_test_print = []
    test_account = 200
    l_test_history = []

    def add_print(x):
        l_test_print.append(x)

    input_data = ["250", "Обувь"]
    monkeypatch.setattr('builtins.input', lambda x: input_data.pop(0))
    monkeypatch.setattr('builtins.print', add_print)
    test_account, l_test_history = ba.purchase(test_account, l_test_history)
    assert test_account == 200
    assert l_test_print[0] == "На вашем счету недостаточно средств для осуществления покупки."

"""
    Тест для функции create_path
"""
def test_create_path():
    s_path_local = "Test"
    s_path_global = "/home"
    s_result = fm.create_path(s_path_local)
    assert s_result == os.getcwd() + "/Test"
    s_result = fm.create_path(s_path_global)
    assert s_result == s_path_global
    s_path_local = "Test/"
    s_result = fm.create_path(s_path_local)
    assert s_result == os.getcwd() + "/Test/"


"""
    Тест для грязной функции create_folder
"""
def test_create_folder(monkeypatch):
    l_test_print = []

    def add_print(x):
        l_test_print.append(x)

    input_data = ["/home/", "test", "1", ]
    monkeypatch.setattr('builtins.input', lambda x: input_data.pop(0))
    monkeypatch.setattr('builtins.print', add_print)
    fm.delete_folder()
    fm.delete_folder()
    fm.delete_folder()
    l_test_print = []
    input_data = ["/home/", "test", "1", ]
    fm.create_folder()
    fm.create_folder()
    fm.create_folder()
    assert l_test_print[0] == "Папка: /home/ успешно создана."
    assert l_test_print[1] == f"Папка: {fm.create_path('test')} успешно создана."
    assert l_test_print[2] == f"Папка: {fm.create_path('1')} успешно создана."


"""
    Тест для грязной функции delete_folder
"""
def test_delete_folder(monkeypatch):
    l_test_print = []

    def add_print(x):
        l_test_print.append(x)

    input_data = ["/home/", "test", "1", ]
    monkeypatch.setattr('builtins.input', lambda x: input_data.pop(0))
    monkeypatch.setattr('builtins.print', add_print)
    fm.create_folder()
    fm.create_folder()
    fm.create_folder()
    l_test_print = []
    input_data = ["/home/", "test", "1", ]
    fm.delete_folder()
    fm.delete_folder()
    fm.delete_folder()
    assert l_test_print[0] == "Папка: /home/ была успешно удалена."
    assert l_test_print[1] == f"Папка: test была успешно удалена."
    assert l_test_print[2] == f"Папка: 1 была успешно удалена."

"""
    Тест для функции получения списка файлов из текущего каталога
"""
def test_get_files_from_current(monkeypatch):
    def mock_list_files(x):
       return ["bank_account.py", "file_manager.py", "quiz.py", "test_filemanager.py"]
    def mock_isfile(x):
       return True
    monkeypatch.setattr(os, 'listdir', mock_list_files)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)
    assert fm.get_files_from_current() == ["bank_account.py", "file_manager.py", "quiz.py", "test_filemanager.py"]


"""
    Тест для функции получения списка каталогов из текущего каталога
"""
def test_get_dirs_from_current(monkeypatch):
    def mock_list_dirs(x):
       return [".git", ".idea", "pytest_cache", "home"]
    def mock_isfile(x):
       return False
    monkeypatch.setattr(os, 'listdir', mock_list_dirs)
    monkeypatch.setattr(os.path, 'isfile', mock_isfile)
    assert fm.get_dirs_from_current() == [".git", ".idea", "pytest_cache", "home"]


 """
     Тест для сохранения текушего каталога
 """
def test_save_current_directory(monkeypatch):
    def mock_get_files():
       return ["bank_account.py", "file_manager.py", "quiz.py", "test_filemanager.py"]
    def mock_get_dirs():
       return [".git", ".idea", "pytest_cache", "home"]
    monkeypatch.setattr(fm, 'get_files_from_current', mock_get_files)
    monkeypatch.setattr(fm, 'get_dirs_from_current', mock_get_dirs)
    fm.save_current_directory()
    with open("listdir.txt","r") as f:
        d_dict = json.load(f)
    assert d_dict["files"] == ["bank_account.py", "file_manager.py", "quiz.py", "test_filemanager.py"]
    assert d_dict["dirs"] == [".git", ".idea", "pytest_cache", "home"]