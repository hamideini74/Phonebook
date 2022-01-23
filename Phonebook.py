class Storage:
    def __init__(self, fname='none', lname='none', phone='none'):
        self.fname = fname
        self.lname = lname
        self.phone = phone

    def save(self, fname, lname, phone):
        with open('phonebook.txt', 'a') as f:
            f.write(f'{fname.title()} {lname} | phone: {phone}')
            f.write('\n')


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
    phone = input('phone number > ')
    storage.save(fname, lname, phone)



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


phone_book()

# import os
# os.system('cls')
