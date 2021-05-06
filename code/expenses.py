

class Expenses():

    def __init__(self, incomes_list):

        self.name_of_incomes_list = incomes_list
        self.dictionary = {}

    def expenses_list(self, object_list):
        x = 0
        # Luo sanakirjan olioiden menojen perusteella.
        for object in object_list:
            name = object.get_name()
            expenses = object.get_expenses_list()
            if not expenses:
                pass
            else:
                sum = 0
                for income in expenses:
                    sum = income + sum
                expenses = sum
                self.dictionary[name] = expenses

        return self.dictionary
