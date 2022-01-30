import json
import re


class Edit:
    def __init__(self):
        pass

    def edit(self, id):
        with open('phonebook.json', 'r+') as f:
            data = json.loads(f.read())
            thisdict = data['contacts']
            for contact in thisdict:
                if int(id) == contact['id']:
                    contact['first_name'] = input('first name > ')
                    contact['last_name'] = input('last name > ')
                    lst = []
                    while True:
                        print('To continue enter "-"')
                        phone = input(f'phone number > ')
                        if re.match(r"(0|\+98)9[0-1]\d{8}", phone):
                            lst.append(phone)
                        elif phone == '-':
                            break
                    contact['phone']=lst
        thisdict[int(id)-1] = contact
        json_phone = json.dumps(data)
        with open('phonebook.json', 'w') as f:
            f.write(json_phone)
            f.write('\n')
        print(contact)
        print('Edit contact successfully!')

