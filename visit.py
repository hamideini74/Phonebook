import json, texttable

class Visit:
    def __init__(self):
        pass

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
            return table.draw()

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
                    table.add_rows([['id', 'first name', 'last name', 'phone'],
                                    [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
                    found = True

            if found == False:
                return f"There's no contact Record in Phonebook with name = {search_contact}"
            return table.draw()
