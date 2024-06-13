
def variants():

    print("1-показать всю историю")
    print("2-почистить всю историю")
    print("3-создать транзакцию")
    print("4-Провести транзакцию")
    print("5-выход")
    num = None

    while num is None:
        try:
            user = int(input("enter num : "))
            print(user)
        except ValueError:
            print("Вы ввели не число")
        except ZeroDivisionError:
            print("лить на ноль нельзя")
        else:
            print("все хорошо")
        finally:
            print("finally")
variants()

