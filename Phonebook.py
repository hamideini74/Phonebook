import re, json
from visualizer import Visualizer
from storage import Storage
from edit import Edit

storage = Storage()
visit = Visualizer()
edit = Edit()


def phone_book():
    while True:
        print('Enter "1" --> Display your contacts \n'
              'Enter "2" --> Creat new contact \n'
              'Enter "3" --> search your contact \n'
              'Enter "4" --> Delete your contact \n'
              'Enter "5" --> Edit your contact \n'
              'Enter "6" --> Quit')
        num = input('your choice -> ')

        if num == '1':
            show()

        elif num == '2':
            fname = input('first name > ')
            lname = input('last name > ')
            lst = []
            while True:
                print('To continue enter "-"')
                phone = input(f'phone number > ')
                if re.match(r"(0|\+98)9[0-1]\d{8}", phone):
                    lst.append(phone)
                elif phone == '-':
                    break
                else:
                    print('please enter phone number correctly ')
            creat_new_contact(fname, lname, lst)

        elif num == '3':
            search_contact = input("Enter fname or lname or phone number for Searching: ")
            search(search_contact)

        elif num == '4':
            key = input('for delete contact by name enter"name" and for delete contact by id enter "id": ')
            if key == "name":
                fname = input('contact first name: ')
                lname = input('contact last name: ')
                name = fname + ' ' + lname
                delete(name)

            elif key == 'id':
                name = input('contact id: ')
                delete(name)

        elif num == '5':
            id = input('enter id for edit contact: ')
            editt(id)

        elif num == '6':
            break


def show():
    with open('phonebook.json', 'r+') as f:
        data = json.loads(f.read())
        thisdict = data['contacts']
        table = visit.contact_list()
        for contact in thisdict:
            table.add_rows([['id', 'first name', 'last name', 'phone'],
                            [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
        print(table.draw())


def creat_new_contact(fname, lname, lst):
    with open('phonebook.json', 'r+') as f:
        data = json.loads(f.read())
        thisdict = data['contacts']
        for contact in thisdict:
            if contact['first_name'] == fname and contact['last_name'] == lname:
                print('These contact have already been registered')
        else:
            storage.save(fname, lname, lst)


def search(search_contact):
    with open('phonebook.json', 'r+') as f:
        found = False
        data = json.loads(f.read())
        thisdict = data['contacts']
        table = visit.contact_list()
        for contact in thisdict:
            if search_contact in contact['first_name'] or search_contact in contact['last_name']:
                table.add_rows([['id', 'first name', 'last name', 'phone'],
                                [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
                found = True
            elif any(search_contact in s for s in contact['phone']):
                table.add_rows([['id', 'first name', 'last name', 'phone'],
                                [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
                found = True
        print(table.draw())

        if found == False:
            return f"There's no contact Record in Phonebook: {search_contact}"


def delete(name):
    delete = storage.delete(name)
    print(delete)


def editt(id):
    edit.edit(id)


phone_book()
