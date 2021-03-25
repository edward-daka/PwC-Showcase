

from readstatement import ReadFile
import income
import expenses

def print_incomes(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
    list_of_transactions = file_object.get_object_list()
    incomes_list = income.Incomes(file_object.get_list_name())
    dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
    total_sum = 0
    pillar = "#"
    for name in dictionary_of_incomes:
        total_sum = total_sum + dictionary_of_incomes[name]
    print("{:<40} | ".format("Names of giver:"),end="")
    print("Percentages")
    print("")
    dictionary_of_incomes = dict(sorted(dictionary_of_incomes.items(), key=lambda item: item[1], reverse=True))
    for name in dictionary_of_incomes:
        print("{:<40} | ".format(name), end="")
        percentage_of_whole = (dictionary_of_incomes[name] / total_sum) * 100
        percentage_of_pillars = round(percentage_of_whole/ 2)
        print((pillar*percentage_of_pillars).ljust(45),end="")
        print("({:.2f}%)".format(percentage_of_whole))



def print_expenses(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
    list_of_transactions = file_object.get_object_list()
    expenses_list = expenses.Expenses(file_object.get_list_name())
    dictionary_of_expenses = expenses_list.expenses_list(list_of_transactions)
    total_sum = 0
    pillar = "#"
    for name in dictionary_of_expenses:
        total_sum = total_sum + dictionary_of_expenses[name]
    print("{:<40} | ".format("Names of receivers:"), end="")
    print("Percentages")
    print("")
    dictionary_of_expenses = dict(sorted(dictionary_of_expenses.items(), key=lambda item: item[1]))
    for name in dictionary_of_expenses:
        print("{:<40} | ".format(name), end="")
        percentage_of_whole = (dictionary_of_expenses[name] / total_sum) * 100
        percentage_of_pillars = round(percentage_of_whole / 2)
        print((pillar * percentage_of_pillars).ljust(21), end="")
        print("({:.2f}%)".format(percentage_of_whole))



def selection_panel():

    print("")
    print("What information would you like to see ?")
    print("1. Show me my Incomes")
    print("2. Show me my Expenses")
    print("3. Quit")
    print("")
    # Tarkistaa että annettu luku on kokonaisluku ja vaihtoehtojen sisällä
    is_correct = True
    while is_correct == True:
        action = (input("Insert the number for the corresponding information:\n"))
        try:
            action = int(action)
            if not (0 <= action <= 3):
                print("Please enter integer from listing above.")
                continue
            else:
                is_correct = False
        except ValueError:
            print("{} is not a integer, please try again.".format(action))
            continue
    print("")
    return action

def main():


      try:
        print("")
        print("Welcome to the money tracker !")
        print("")
        file_to_open = input("Enter the name of the statement file:\n")
        file_object = ReadFile(file_to_open)
        file_object.read_file(file_to_open)
        next_action = selection_panel()
        while next_action != 3:
            if next_action == 1:
               print_incomes(file_object)
            elif next_action == 2:
               print_expenses(file_object)
            next_action = selection_panel()
        print("Thank you for testing!")
      except OSError:
          print("Error in reading the file.")



main()



