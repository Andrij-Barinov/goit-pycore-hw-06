from collections import UserDict

class Field:
    # Base class for all fields
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Class for storing a contact name
    pass

class Phone(Field):
    # Class for storing phone numbers with validation
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    # Class for storing records (contacts)
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        # Method for adding a phone number
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        # Method to delete a phone number
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        # Method for editing a phone number
        self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def __str__(self):
        # Method for formatovaniy vyvodu zapisu
        phones = ', '.join(str(phone) for phone in self.phones)
        return f"{self.name.value}: {phones}"

class AddressBook(UserDict):
    # Class for storing an address book
    def add_record(self, record):
        # Method for adding a record
        self.data[record.name.value] = record

    def find(self, name):
        # Method to search for a record by name
        return self.data.get(name)

    def delete(self, name):
        # Method to delete a record by name
        if name in self.data:
            del self.data[name]