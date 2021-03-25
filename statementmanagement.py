
class StatementManagement():
    def __init__(self, transaction_name):
        self.__name = transaction_name
        self.__transactions = []
        self.__incomes = []
        self.__expenses = []
        self.__messages = []

    def add_transaction(self, value):
        # lisää transaktion tuloihin ja menoihin, ellei se ole sisäinen siirto
        self.__transactions.append(value)
        if len(self.__messages) == 0:
            pass
        elif self.__messages[len(self.__messages) - 1] == "Omasiirto":
            pass
        elif value >= 0:
            self.__incomes.append(value)
        else:
            self.__expenses.append(value)

    def add_message(self,message):
        self.__messages.append(message)

    def get_name(self):
        return self.__name

    def get_messages(self):
        return self.__messages

    def get_transaction_list(self):
        return self.__transactions

    def get_incomes_list(self):
        return self.__incomes
    def get_expenses_list(self):
        return self.__expenses


