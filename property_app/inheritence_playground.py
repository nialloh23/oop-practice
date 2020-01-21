
class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
            return matching_contacts



class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone_number):
        super().__init__(name, email)
        self.phone_number = phone_number


