

from readstatement import ReadFile
import income
import expenses
from grouping import Grouping
def print_incomes(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
 if file_object.get_income_group():
    grouped_or_not = input("Do you want to show the transaction grouped or not ? (y/n) \n")

    if grouped_or_not == "n":
        list_of_transactions = file_object.get_object_list()
        incomes_list = income.Incomes(file_object.get_list_name())
        dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
        if not dictionary_of_incomes:
            print("No incomes found")
        else:
            print_graph(dictionary_of_incomes,True)

    elif grouped_or_not == "y":
         list_of_transactions = file_object.get_object_list()
         incomes_list = income.Incomes(file_object.get_list_name())
         dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
         group_list = file_object.get_income_group()
         grouped_items = Grouping(file_object.get_list_name())
         dictionary_of_groups,already_listed = grouped_items.create_dictionary(group_list)
         dictionary_of_incomes.update(dictionary_of_groups)
         for items in already_listed:
             try:
                dictionary_of_incomes.pop(items)
             except KeyError:
                print("Caution : You've added the same transaction to twice into groups!")
         type = True
         print_graph(dictionary_of_incomes,type)
    else:
        print("Error: Please select 'y' or 'n' (yes/no). Try again !")
 else:
        list_of_transactions = file_object.get_object_list()
        incomes_list = income.Incomes(file_object.get_list_name())
        dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
        if not dictionary_of_incomes:
            print("No incomes found.")
        else:
            print_graph(dictionary_of_incomes,True)



def print_graph(dictionary,type):
    total_sum = 0
    pillar = "#"
    for name in dictionary:
        total_sum = total_sum + dictionary[name]
    if type == True:
        print("{:<45} | ".format("Names of giver:"), end="")
    else:
        print("{:<45} | ".format("Names of receivers:"), end="")
    print("Percentages")
    print("")
    if type == True:
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    else:
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    for name in dictionary:
        print("{:<45} | ".format(name), end="")
        percentage_of_whole = (dictionary[name] / total_sum) * 100
        percentage_of_pillars = round(percentage_of_whole / 2)
        print((pillar * percentage_of_pillars).ljust(50), end="")
        print(round(dictionary[name],1),"€",end="")
        print(" ({:<.2f}%)".format(percentage_of_whole))






def print_expenses(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
    if file_object.get_expense_group():
        grouped_or_not = input("Do you want to show the transaction grouped or not ? (y/n) \n")
        if grouped_or_not == "n":
            list_of_transactions = file_object.get_object_list()
            expenses_list = expenses.Expenses(file_object.get_list_name())
            dictionary_of_expenses = expenses_list.expenses_list(list_of_transactions)
            if not dictionary_of_expenses:
                print("No expenses found.")
            else:
                print_graph(dictionary_of_expenses, False)

        elif grouped_or_not == "y":
            list_of_transactions = file_object.get_object_list()
            expenses_list = expenses.Expenses(file_object.get_list_name())
            dictionary_of_expenses = expenses_list.expenses_list(list_of_transactions)
            group_list = file_object.get_expense_group()
            grouped_items = Grouping(file_object.get_list_name())
            dictionary_of_groups, already_listed = grouped_items.create_dictionary(group_list)
            dictionary_of_expenses.update(dictionary_of_groups)
            for items in already_listed:
                try:
                    dictionary_of_expenses.pop(items)
                except KeyError:
                    print("Caution : You've added the same transaction to twice into groups!")
            type = False
            print_graph(dictionary_of_expenses, type)
        else:
            print("Error: Please select 'y' or 'n' (yes/no). Try again !")

    else:
        list_of_transactions = file_object.get_object_list()
        expenses_list = expenses.Expenses(file_object.get_list_name())
        dictionary_of_expenses = expenses_list.expenses_list(list_of_transactions)
        if not dictionary_of_expenses:
            print("No expenses found.")
        else:
            print_graph(dictionary_of_expenses,False)





def selection_panel():

    print("")
    print("What information would you like to see ?")
    print("1. Show me my Incomes")
    print("2. Show me my Expenses")
    print("3. How much more can I earn ?")
    print("4. Group transactions ?")
    print("5. Quit")
    print("")
    # Tarkistaa että annettu luku on kokonaisluku ja vaihtoehtojen sisällä
    is_correct = True
    while is_correct:
        action = (input("Insert the number for the corresponding information:\n"))
        try:
            action = int(action)
            if not (0 <= action <= 5):
                print("Please enter integer from listing above.")
                continue
            else:
                is_correct = False
        except ValueError:
            print("{} is not a integer, please try again.".format(action))
            continue
    print("")
    return action

def kelacalculator(file_object):

    kela_months = {1 : 23554, 2 : 22172, 3 : 20790, 4 : 19408, 5 : 18026, 6 : 16644, 7 : 15262, 8 : 13880, 9 : 12498, 10 : 11116, 11 : 9734, 12 : 8352,}

    print("I'll help you calculate how much more you can earn")
    print("before you'll need to contact KELA regarding your student benefits.")
    print("")
    is_correct = True
    while is_correct:
        benefit_months = (input("How many benefit months do you have during the year ? \n"))
        try:
            benefit_months = int(benefit_months)
            if not (1 <= benefit_months <= 12):
                print("Please enter an integer between 1 and 12.")
                continue
            else:
                limit = (kela_months[benefit_months])
                it_correct = True
                while it_correct:
                    already_earned = (input("How much have you already earned during the year ? \n"))
                    try:
                        already_earned = float(already_earned)
                        if already_earned >= limit:
                            print("You've earned your limit. Please contact KELA for further instructions. https://www.kela.fi/asiakaspalvelu")


                        else:
                            list_of_transactions = file_object.get_object_list()
                            incomes_list = income.Incomes(file_object.get_list_name())
                            dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
                            total_sum = 0
                            i = 0
                            for name in dictionary_of_incomes:
                                total_sum = total_sum + dictionary_of_incomes[name]
                            while already_earned <= limit:
                                already_earned = already_earned + total_sum
                                i = i + 1
                            if i >= 12:
                                print("With your current earnings of {:.2f} € you won't need to check your students benefits for at least 1 year.".format(total_sum))
                            else:
                                print("With your current earnings of {:.2f} € you'll need to check your student benefits in {} months.".format(total_sum,i))
                            is_correct = False
                            it_correct = False
                    except ValueError:
                        print(already_earned, "isn't an float or integer. Please enter the correct number.")

        except ValueError:
            print(benefit_months,"is not an integer. Please enter an integer between 1 and 12.")

def group_it(file_object):

    print("In this part of the program, you can group transactions.")
    grouped_objects = []
    all_grouped = False
    while not all_grouped:
        name_of_group = input("What is the name of your group ?\n")
        grouped_items = (Grouping(name_of_group))
        object_list = file_object.get_object_list()
        type_given = False
        while not type_given:
            type = input("Are the added transactions expenses or incomes ?\n")
            if type == "incomes":
               file_object.add_to_income_group(grouped_items)
               grouped_items.add_transaction_to_group(object_list,True)
               type_given = True
               break
            elif type == "expenses":
               file_object.add_to_expenses_group(grouped_items)
               grouped_items.add_transaction_to_group(object_list,False)
               type_given = True
               break
            else:
                print("Please input 'incomes' or 'expenses'")
        more_group = True
        while more_group:
            next_step = input("Would you like to make more groups ? (y/n)\n")

            if next_step == "y":
               pass
               more_group = False
            elif next_step == "n":
               all_grouped = True
               more_group = False
            else:
                print("Please input 'y' or 'n' (yes/no)")


def main():
    reading_file = True
    print("")
    print("Welcome to the money tracker !")
    print("")
    while reading_file == True:
      try:
        file_to_open = input("Enter the name of the statement file:\n")
        if file_to_open[-3:] != "csv":
            print("We can only handle files in 'csv' format!")
        file_object = ReadFile(file_to_open)
        file_object.read_file(file_to_open)

        next_action = selection_panel()
        while next_action != 5:
            if next_action == 1:
               print_incomes(file_object)
            elif next_action == 2:
               print_expenses(file_object)
            elif next_action == 3:
              kelacalculator(file_object)
            elif next_action == 4:
              group_it(file_object)
            next_action = selection_panel()
        print("Thank you for testing!")
        reading_file = False
      except OSError:
          print("Error in reading the file:",file_to_open)
          print("Please try again !")
          print("")



main()



