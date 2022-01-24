import json


class Storage:

    def __init__(self):
        pass
        # self.fname = fname
        # self.lname = lname
        # self.phone = phone

    def save(self, fname, lname, phone1, phone2='none'):
        with open('phonebook.json', 'r+') as f:
            data = json.loads(f.read())
            id = data['last_id']
            phone_dict = {'first_name': fname, 'last_name': lname, 'phone': [phone1, phone2], 'id': id}
            data['contacts'].append(phone_dict)
            data['last_id'] += 1
        json_phone = json.dumps(data)
        with open('phonebook.json', 'w') as f:
            f.write(json_phone)
            f.write('\n')

    def load(self, name):
        f = open('phonebook.json', "r+")
        found = False

        data = json.loads(f.read())
        thisdict = data['contacts']
        for contact in thisdict:
            if contact['first_name'] == name:
                print(contact)
            found = True

        if found == False:
            print(f"There's no contact Record in Phonebook with name = {name}")
        f.close()

    def delete(self, fname, lname):
        f = open('phonebook.json', "r+")
        data = json.loads(f.read())
        thisdict = data['contacts']
        for contact in thisdict:
            if contact['first_name'] == fname and contact['last_name'] == lname:
                thisdict.remove(contact)
        f.close()


storage = Storage()


def phone_book():
    while True:
        print('Enter "1" --> Display your contacts \n'
              'Enter "2" --> Creat new contact \n'
              'Enter "3" --> search your contact \n'
              'Enter "4" --> Delete your contact \n'
              'Enter "5" --> Quit')
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
    with open('phonebook.json', 'r') as f:
        print(f.read())


def delete():
    fname = input('contact first name: ')
    lname = input('contact last name: ')
    storage.delete(fname, lname)


def search():
    name = input("Enter name for Searching: ")
    storage.load(name)


phone_book()

# import os
# os.system('cls')
