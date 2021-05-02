import readstatement
import income
class Grouping():

    def __init__(self,group_name):
        self.group_name = group_name
        self.grouped_transactions = []
        self.total_grouped_transactions = 0
        self.added_transactions = []
        self.dictionary = {}

    def add_transaction_to_group(self,object_list,transaction_type):
        added_transaction = ""
        while added_transaction != "STOP":
            added_transaction = input("What transaction would you like to add ?\n")
            passed = 0
            for object in object_list:
                name = object.get_name()
                if name == added_transaction:
                   self.added_transactions.append(name)
                   if transaction_type == True:
                       incomes_list = object.get_incomes_list()
                       for income in incomes_list:
                        self.grouped_transactions.append(income)
                        self.total_grouped_transactions += income
                   else:
                       expenses_list = object.get_expenses_list()
                       for expense in expenses_list:
                           self.grouped_transactions.append(expense)
                           self.total_grouped_transactions += expense
                else:
                    passed = passed + 1
                    if passed == len(object_list):
                        print("Couldn't find that transaction in the file.")

    def create_dictionary(self,grouplist):
        for object in grouplist:
         name = object.group_name
         self.dictionary[name] = object.total_grouped_transactions
         self.added_transactions.extend(object.added_transactions)

        return self.dictionary, self.added_transactions




