import re
from visit import Visit
from storage import Storage


storage = Storage()
visit = Visit()


def phone_book():
    global lst
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
            fname = input('contact first name: ')
            lname = input('contact last name: ')
            id = input('contact id: ')
            delete(fname, lname, id)

        elif num == '5':
            break


def creat_new_contact(fname, lname, lst):
    storage.save(fname, lname, lst)


def show():
    table = visit.contact_list()
    print(table)


def delete(fname, lname, id):
    delete = storage.delete(fname, lname, id)
    print(delete)


def search(search_contact):
    search = visit.load(search_contact)
    print(search)


phone_book()
