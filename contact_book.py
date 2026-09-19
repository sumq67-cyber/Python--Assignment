#Assignment # 04
# Topic: Build a Contact Book in Python

contact_book = {}
#function to add a new contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
 #store contact in dictionary
    contact_book[name] = {
        'Phone': phone,
        'Email': email
        }

   #search contact in dictionary
def search_contact():
    name = input("Enter the name to search: ")
    if name in contact_book:
        contact = contact_book[name]
        print("\nContact Found!")
        print(f"Name: {name}")
        print(f"Phone: {contact['Phone']}")
        print(f"Email: {contact['Email']}")
    else:
        print(f"{name} not found in the contact book.")

    #funtion to display contacts
def view_contact():

    if not contact_book:
        print("No contacts available.")
        return

    print("\n--- All Contacts ---")

    # Loop through all contacts
    for name, information in contact_book.items():
        print("Name:", name)
        print("Phone:", information["Phone"])
        print("Email:", information["Email"])
        print("--------------------")

  #main
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        view_contact()
    elif choice == '4':
        print("Exiting the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
