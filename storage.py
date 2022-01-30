import json


class Storage:

    def __init__(self):
        pass

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

    def delete(self, name):
        with open('phonebook.json', 'r+') as f:
            data = json.loads(f.read())
            thisdict = data['contacts']
            for contact in thisdict:
                ls = name.split()
                if contact['first_name'] == ls[0] and contact['last_name'] == ls[1]:
                    thisdict.remove(contact)
                    json_phone = json.dumps(data)
                    with open('phonebook.json', 'w') as f:
                        f.write(json_phone)
                        f.write('\n')
                    return 'Delete contact successfully!'
                elif str(contact['id']) == name:
                    thisdict.remove(contact)
                    json_phone = json.dumps(data)
                    with open('phonebook.json', 'w') as f:
                        f.write(json_phone)
                        f.write('\n')
                    return 'Delete contact successfully!'
            else:
                return 'Contact not found'
