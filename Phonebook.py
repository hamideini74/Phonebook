import json, re, texttable


class Storage:

    def __init__(self):
        pass
        # self.fname = fname
        # self.lname = lname
        # self.phone = phone

    def contact_list(self):
        with open('phonebook.json', 'r') as f:
            data = json.loads(f.read())
            thisdict = data['contacts']
            table = texttable.Texttable(max_width=0)
            table.set_cols_align(['l', 'c', 'c', 'r'])
            table.set_cols_valign(['t', 'm', 'm', 'b'])
            for contact in thisdict:
                table.add_rows([['id', 'first name', 'last name', 'phone'],
                                [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
            print(table.draw())

    def save(self, fname, lname, lst):
        with open('phonebook.json', 'r+') as f:
            data = json.loads(f.read())
            id = data['last_id']
            phone_dict = {'first_name': fname, 'last_name': lname, 'phone': lst, 'id': id}
            data['contacts'].append(phone_dict)
            data['last_id'] += 1
        json_phone = json.dumps(data)
        with open('phonebook.json', 'w') as f:
            f.write(json_phone)
            f.write('\n')

    def load(self, search_contact):
        with open('phonebook.json', 'r+') as f:
            found = False
            data = json.loads(f.read())
            thisdict = data['contacts']
            table = texttable.Texttable(max_width=0)
            table.set_cols_align(['l', 'c', 'c', 'r'])
            table.set_cols_valign(['t', 'm', 'm', 'b'])
            for contact in thisdict:
                if contact['first_name'] == search_contact or contact['last_name'] == search_contact or \
                        contact['phone'][0] == search_contact:
                    # contact['phone'][1] == search_contact:
                    table.add_rows([['id', 'first name', 'last name', 'phone'],
                                    [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
                    found = True

            if found == False:
                print(f"There's no contact Record in Phonebook with name = {search_contact}")
            # table_draw = table.draw()
            print(table.draw())

    def delete(self, fname, lname):
        f = open('phonebook.json', "r+")
        data = json.loads(f.read())
        thisdict = data['contacts']
        for contact in thisdict:
            if contact['first_name'] == fname and contact['last_name'] == lname:
                thisdict.remove(contact)
                json_phone = json.dumps(data)
                with open('phonebook.json', 'w') as f:
                    f.write(json_phone)
                    f.write('\n')
                    return 'successfully'

        f.close()


storage = Storage()


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
            for i in range(1, 3):
                print('To continue enter "-"')
                phone = input(f'phone number {i}> ')
                if re.match(r"(0|\+98)9[0-1]\d{8}", phone):
                    lst.append(phone)
                elif phone == '-':
                    continue
                else:
                    print('please enter phone number correctly ')
            creat_new_contact(fname, lname, lst)

        elif num == '3':
            search_contact = input("Enter fname or lname or phone number for Searching: ")
            # lname = input("Enter last name for Searching: ")
            # phone = input("Enter phone for Searching: ")
            search(search_contact)

        elif num == '4':
            fname = input('contact first name: ')
            lname = input('contact last name: ')
            delete(fname, lname)

        elif num == '5':
            break


def creat_new_contact(fname, lname, lst):
    storage.save(fname, lname, lst)


def show():
    storage.contact_list()


def delete(fname, lname):
    storage.delete(fname, lname)


def search(search_contact):
    storage.load(search_contact)


phone_book()
