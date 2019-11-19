import json as js
import os

"""
   Функция пополнения счета
   Параметры:
   account - Счет, на который будут зачислены средства
   history - История работы со счетом
"""
def refill(account, history):
    try:
        i_refill_amount = int(input("Введите сумму пополнения счета: "))
    except ValueError as ex:
        print(f"Неверная сумма пополнения счета.")
        history.append("Неверная сумма пополнения счета.")
        return account, history
    history.append(f"Счет пополнен на {i_refill_amount} рублей.")
    print(f"Счет пополнен на {i_refill_amount} рублей.")
    return account + i_refill_amount, history

"""
   Функция для осуществления покупки
   Параметры:
   account - Счет для осуществления покупки
   history - История работы со счетом
"""
def purchase(account, history):
    s_purchase_amount = input("Введите сумму покупки: ")
    # Здесь в качестве практики обработка неправильного ввода
    # сделана с использованием функции isdigit, хотя может быть
    # использован механизм обработки исключений
    if s_purchase_amount.isdigit():
        i_purchase_amount = int(s_purchase_amount)
    else:
        print(f'Сумма покупки введена неверно.')
        history.append(f"Сумма покупки введена неверно.")
        return account, history
    if account - i_purchase_amount < 0:
        print("На вашем счету недостаточно средств для осуществления покупки.")
        return account, history
    else:
        s_name_purchase = input("Введите название покупки:")
        history.append(f"Совершена покупка \"{s_name_purchase}\" на сумму {i_purchase_amount}.")
        print(f"Покупка успешно совершена. На счету осталось {account-i_purchase_amount}.")
    return account - i_purchase_amount, history


"""
   Функция вывода на печать истории работы со счетом
   Параметры:
   history - История работы со счетом
"""
def print_history(history):
    for s_element_history in history:
        print(s_element_history)
    return


"""
   Главная функция приложения bank_account
"""
def bank_account():
    s_file_name = "bankaccount.json"
    # Проверить наличие файла с сохраненными данными и загрузить его если он сущеуствует
    if os.path.exists(s_file_name):
        with open(s_file_name,"r") as f:
            l_archive = js.load(f)
            account = l_archive[0]
            history = l_archive[1]
    else:
        account = 0
        history = []

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню:')
        if choice == '1':
            account, history = refill(account, history)
        elif choice == '2':
            account, history = purchase(account, history)
        elif choice == '3':
            print_history(history)
        elif choice == '4':
            with open(s_file_name, "w") as f:
                l_archive = [account, history]
                js.dump(l_archive,f)
            break
        else:
            print('Неверный пункт меню')


if __name__ == "__main__":
    bank_account()
