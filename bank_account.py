
"""
   Функция пополнения счета
   Параметры:
   account - Счет, на который будут зачислены средства
   history - История работы со счетом
"""
def refill(account, history):
    i_refill_amount = int(input("Введите сумму пополнения счета: "))
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
    i_purchase_amount = int(input("Введите сумму покупки: "))
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

def bank_account():

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
            break
        else:
            print('Неверный пункт меню')
