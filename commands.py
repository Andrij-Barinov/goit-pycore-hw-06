from utils import input_error
from models import AddressBook, Record

@input_error
def add_contact(args, contacts):
    # Adds a new contact
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Changes an existing contact
    name, phone = args
    record = contacts.find(name)
    if record:
        record.edit_phone(record.phones[0].value, phone)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    # Shows phone number by name
    name = args[0]
    record = contacts.find(name)
    if record:
        return ', '.join(phone.value for phone in record.phones)
    else:
        return "Contact not found."

def show_all(contacts):
    # Shows all contacts
    return "\n".join(str(record) for record in contacts.data.values())