"""Create a PhoneBook Application app using python which save,search,delete and list all numbers 
using conditional statements , dictionaries and loops    """

# make phonebook.py file in your code editer
# make a empty dictionary

Phonebook={}

# make a logic  to add  contact.
def add_contact():
    name= input("Enter the contact name: ").strip()
    if name in Phonebook:
        print(f"Contact '{name}' already exist.")

    else:
        phone=input("Enter the phone number: ").strip()
        Phonebook[name]= phone
        print(f"Contact '{name}' added successfuly.")

# make a logic to search contact
def search_contact():
    name= input("Enter the contact name you want to search: ").strip()
    if name in Phonebook:
        print(f"Contact '{name}': {Phonebook[name]} .")
    else:
        print(f"Contact '{name}' Not Found.")

# make logic for delete contact
def delete_contact():
    name= input("Enter the contact of contact you want to delete: ").strip()
    if name in Phonebook:
        del Phonebook[name]
        print(f"{name} deleted successfuly.")
    else:
        print(f"Contact '{name}' Not Found.")

# make logic to list all contact to user
def list_contact():
    if not Phonebook:
        print("Phonebook is empty.")
    else:
        print("--- All Contacts ---")
# for continue showing menu,we will iterate a loop on a dictinary
        for name, phone in Phonebook.items():
            print(f"{name}: {phone}")

# user interface
"""  Implement a loop that continuously displays a menu of options to the user until they choose to exit. Use input() 
to read the user's choice and if-else statements to handle different actions based on the choice."""

while True:
    print("\n ---- PhoneBook Menu ----")
    print("1. Add a New Contact")
    print("2. Search For a New Contact")
    print("3. Delete Contact")
    print("4. List All Contacts")
    print("5. Exit")
    choice= input("Enter the choice from (1-5) :").strip()

    if choice == '1':
        print(add_contact())
    elif choice == '2':
        print(search_contact())
    elif choice == '3':
        print(delete_contact())
    elif choice == '4':
        print(list_contact())
    elif choice == '5':
        print("Exititing PhoneBook. GoodBye.")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
#                project has finished