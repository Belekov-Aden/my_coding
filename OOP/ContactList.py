class ContactList(list):

    def __init__(self, list):
        self.list = list
        self.new = []

    def search_by_name(self, name):
        for i in self.list:
            if i == name:
                self.new.append(i)

        return f'Совпадение `{name}` в списке {self.list}\n{self.new} - {len(self.new)}'


all_contacts = ContactList(['name', 'aden', 'aden', 'zoo', 'zoo', 'aden'])
print(all_contacts.search_by_name('aden'))
