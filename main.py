from commands import add_contact, change_contact, show_phone, show_all
from utils import parse_input, input_error
from models import AddressBook

def main():
    # The main function for launching a bot
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Ending the work of the bot
            print("Good bye!")
            break
        elif command == "hello":
            # Welcome to the user
            print("How can I help you?")
        elif command == "add":
            # Add a contact
            print(add_contact(args, contacts))
        elif command == "change":
            # Change an existing contact
            print(change_contact(args, contacts))
        elif command == "phone":
            # Search for a phone by name
            print(show_phone(args, contacts))
        elif command == "all":
            # Show all contacts
            print(show_all(contacts))
        else:
            # Unknown team
            print("Invalid command.")

if __name__ == "__main__":
    main()