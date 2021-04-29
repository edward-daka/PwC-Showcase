import csv
import statementmanagement

class ReadFile():

    def __init__(self, file_name):

        self.__file_name = file_name
        self.list_of_transaction_objects = []
        self.list_of_grouped_objects = []

    def read_file(self, file_to_open):
        # Lukee tiedoston, luoden tilitapahtumille oliot.
        with open(file_to_open) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            header_row = next(csv_reader)
            names = []
            amounts = []
            incomes = []
            expenses = []
            for row in csv_reader:
                # Lukee ensin csv.tiedostolta tilitapahtuman nimen
                name = str(row[5])

                # Jos nimi ei ole vielä listalla, niin luo uuden olion
                if name not in names:
                    names.append(name)

                    self.list_of_transaction_objects.append(statementmanagement.StatementManagement(name))
                    # Lukee tilitapahtumaa koskevan viestin
                    messages = row[8]
                    messages = messages.replace(" ", "")
                    messages_split = messages.split(":")
                    if len(messages_split) <= 1:
                        pass
                    else:
                        message_info = messages_split[1]
                        self.list_of_transaction_objects[len(self.list_of_transaction_objects) - 1].add_message(
                            message_info)
                    amount = float(row[2])
                    amounts.append(amount)
                    self.list_of_transaction_objects[len(self.list_of_transaction_objects) - 1].add_transaction(amount)
                # Jos on olemassa jo saman niminen tilitapahtuma, lisätään siihen vain uusi transaktio ja viesti
                else:
                    for object in self.list_of_transaction_objects:
                        transaction_name = object.get_name()
                        if transaction_name == name:
                            messages = row[8]
                            messages = messages.replace(" ", "")
                            messages_split = messages.split(":")
                            if len(messages_split) <= 1:
                                pass
                            else:
                                message_info = messages_split[1]
                                object.add_message(message_info)
                            object.add_transaction(float(row[2]))
                        else:
                            pass
    def add_to_group(self,name):
        self.list_of_grouped_objects.append(name)


    def get_object_list(self):
        # palauttaa listan luoduista olioista

        return self.list_of_transaction_objects

    def get_group_list(self):

        return self.list_of_grouped_objects

    def get_list_name(self):
        # palauttaa oliolistan/tiedoston nimen
        return self.__file_name

