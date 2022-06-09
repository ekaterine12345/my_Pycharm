class BankAccount:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def get_account_name(self):
        return self.__account_name

    def set_account_name(self, user_name):
        self.__account_name = user_name
        print(user_name)

    def deposit(self, new_money):
        self.__balance += new_money
        return f"თანხის შეტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი"

    def withdraw(self, go_money):
        if go_money <= self.__balance:
            self.__balance -= go_money
            return f"თანხის გამოტანა შესრულებულია. ამჟამად თქვენ ანგარიშზე გაქვთ {self.__balance} ლარი"
        else:
            return "თანხა საკმარისი არ არის"


username = input("შეიტანეთ კლიენტის სახელი და გვარი: ")
current_money = int(input("რა თანხა გაქვთ ამჟამათ ანგარიშზე? "))
bank_Account = BankAccount(username, current_money)
# bank_Account.set_account_name=username
operation = int(input('''შეიტანეთ შესაბამისი კოდი რომელი ოპერაციის შესრულება გსურთ:
თანხის შეტანა 1, თანხის გამოტანა 2 '''))
if operation == 1:
    new_money = int(input(f"{bank_Account.get_account_name()} რა თანხის შეტანა გსურთ? "))
    print(bank_Account.deposit(new_money))
elif operation == 2:
    go_money = int(input(f"{bank_Account.get_account_name()} რა თანხის გატანა გსურთ? "))
    print(bank_Account.withdraw(go_money))
