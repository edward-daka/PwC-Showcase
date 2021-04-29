

from readstatement import ReadFile
import income
import expenses
from grouping import Grouping
def print_incomes(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
 if file_object.get_group_list():
    grouped_or_not = input("Do you want to show the transaction grouped or not ? (y/n) \n")

    if grouped_or_not == "n":
        list_of_transactions = file_object.get_object_list()
        incomes_list = income.Incomes(file_object.get_list_name())
        dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
        print_graph(dictionary_of_incomes)

    elif grouped_or_not == "y":
         list_of_transactions = file_object.get_object_list()
         incomes_list = income.Incomes(file_object.get_list_name())
         dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
         group_list = file_object.get_group_list()
         grouped_items = Grouping(file_object.get_list_name())
         dictionary_of_groups,already_listed = grouped_items.create_dictionary(group_list)
         dictionary_of_incomes.update(dictionary_of_groups)
         for items in already_listed:
             dictionary_of_incomes.pop(items)
         type = True
         print_graph(dictionary_of_incomes,type)
 else:
        list_of_transactions = file_object.get_object_list()
        incomes_list = income.Incomes(file_object.get_list_name())
        dictionary_of_incomes = incomes_list.incomes_list(list_of_transactions)
        print_graph(dictionary_of_incomes,True)


def print_graph(dictionary,type):
    total_sum = 0
    pillar = "#"
    for name in dictionary:
        total_sum = total_sum + dictionary[name]
    if type == True:
        print("{:<40} | ".format("Names of giver:"), end="")
    else:
        print("{:<40} | ".format("Names of receivers:"), end="")
    print("Percentages")
    print("")
    if type == True:
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    else:
        dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    for name in dictionary:
        print("{:<40} | ".format(name), end="")
        percentage_of_whole = (dictionary[name] / total_sum) * 100
        percentage_of_pillars = round(percentage_of_whole / 2)
        print((pillar * percentage_of_pillars).ljust(45), end="")
        print("({:.2f}%)".format(percentage_of_whole))






def print_expenses(file_object):

    # Luo Expenses-luokkaa hyödyntäen sanakirjat menoista, ja tulostaa niistä jaottelun suurimmasta pienimpään.
    if
    list_of_transactions = file_object.get_object_list()
    expenses_list = expenses.Expenses(file_object.get_list_name())
    dictionary_of_expenses = expenses_list.expenses_list(list_of_transactions)
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
    while is_correct == True:
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

    kela_months = {"1": 23554, "2" : 22172, "3" : 20790,"4" : 19408,"5" : 18026,"6" : 16644,"7" : 15262,"8" : 13880,"9" : 12498,"10" : 11116,"11" : 9734,"12" : 8352,}

    print("I'll help you calculate how much more you can earn")
    print("before you'll need to contact KELA regarding your student benefits.")
    print("")
    benefit_months = str(input("How many benefit months do you have during the year ? \n"))
    limit = (kela_months[benefit_months])
    already_earned = int(input("How much have you already earned during the year ?\n"))
    if already_earned > limit:
        print("You've already earned beyond your limit. Please contact KELA for further instructions. https://www.kela.fi/asiakaspalvelu")
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
        print("With your current earnings of {} € you'll need to check your student benefits in {} months.".format(total_sum,i))

def group_it(file_object):

    print("In this part of the program, you can group transactions.")
    grouped_objects = []
    all_grouped = False
    while all_grouped == False:
        name_of_group = input("What is the name of your group ?\n")
        grouped_items = (Grouping(name_of_group))
        file_object.add_to_group(grouped_items)
        object_list = file_object.get_object_list()
        type_given = False
        while type_given == False:
            type = input("Are the added transactions expenses or incomes ?")
            if type == "incomes":
               grouped_items.add_transaction_to_group(object_list,True)
               type_given == True
            elif type == "expenses":
               grouped_items.add_transaction_to_group(object_list,False)
               type_given == True
            else:
                print("Please input 'incomes' or 'expenses'")
        next_step = input("Would you like to make more groups ? (y/n)")

        if next_step == "y":
           pass
        if next_step == "n":
           all_grouped = True


def main():


      try:
        print("")
        print("Welcome to the money tracker !")
        print("")
        file_to_open = input("Enter the name of the statement file:\n")
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
      except OSError:
          print("Error in reading the file.")



main()



