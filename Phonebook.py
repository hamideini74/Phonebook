import json


class Storage:

    def __init__(self):
        pass
        # self.fname = fname
        # self.lname = lname
        # self.phone = phone

    def save(self, fname, lname, phone1, phone2='none'):
        phone_dict = {'last_id': 1,'contacts': [{'first_name': fname, 'last_name': lname, 'phone': [phone1, phone2]}]}
        json_phone = json.dumps(phone_dict)
        with open('phonebook.txt', 'a') as f:
            f.write(json_phone)
            f.write('\n')

    def load(self, name):
        f = open('phonebook.txt', "r+")
        contents = f.readlines()
        found = False

        for line in contents:
            if name in line:
                print(f"Your Required Contact Record is: {line}")
                found = True

        if found == False:
            print(f"There's no contact Record in Phonebook with name = {name}")
        f.close()


storage = Storage()


def phone_book():
    print('Enter "1" --> Display your contacts \n'
          'Enter "2" --> Creat new contact \n'
          'Enter "3" --> search your contact \n'
          'Enter "4" --> Delete your contact \n'
          'Enter "5" --> Quit')
    while True:
        num = input('your choice -> ')

        if num == '1':
            show()
        elif num == '2':
            creat_new_contact()
        elif num == '3':
            search()
        elif num == '4':
            delete()
        elif num == '5':
            break


def creat_new_contact():
    fname = input('first name > ')
    lname = input('last name > ')
    phone1 = input('phone number 1> ')
    phone2 = input('phone number 2> ')
    storage.save(fname, lname, phone1, phone2)


def show():
    with open('phonebook.txt', 'r') as f:
        print(f.read())


def delete():
    contact = input('contact name: ')
    f = open('phonebook.txt', 'r+')
    lines = f.readlines()
    for line in lines:
        if contact.title() in lines:
            f.write(line)


def search():
    name = input("Enter name for Searching: ").title()
    storage.load(name)


phone_book()

# import os
# os.system('cls')
