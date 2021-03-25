

class Incomes():

    def __init__(self, incomes_list):

        self.name_of_incomes_list = incomes_list
        self.dictionary = {}

    def incomes_list(self,object_list):
        x = 0
        # Luo sanakirjan olioiden tulojen perusteella
        for object in object_list:
         name = object.get_name()
         incomes = object.get_incomes_list()
         if not incomes:
             pass
         else:
                sum = 0
                for income in incomes:
                    sum = income + sum
                incomes = sum
                self.dictionary[name] = incomes

        return self.dictionary








