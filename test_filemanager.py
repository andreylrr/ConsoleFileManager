import bank_account as ba
import filemanager as fm
import os

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
