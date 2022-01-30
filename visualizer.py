import texttable


class Visualizer:
    def __init__(self):
        pass

    def contact_list(self):
        table = texttable.Texttable(max_width=0)
        table.set_cols_align(['l', 'c', 'c', 'r'])
        table.set_cols_valign(['t', 'm', 'm', 'b'])
        # for contact in thisdict:
        #     table.add_rows([['id', 'first name', 'last name', 'phone'],
        #                     [contact['id'], contact['first_name'], contact['last_name'], contact['phone']]])
        return table
