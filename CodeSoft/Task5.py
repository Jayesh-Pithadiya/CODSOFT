# Contact Book Application

contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

# Function to display all contacts
def view_contacts():
    if contacts:
        print("\nContact List:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}")
    else:
        print("No contacts found.")

# Function to search for a contact by name or phone
def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact["name"] or search_term in contact["phone"]]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

# Function to update contact details
def update_contact():
    search_term = input("Enter the name or phone number of the contact to update: ")
    for contact in contacts:
        if search_term == contact["name"] or search_term == contact["phone"]:
            print("Contact found. Enter new details (leave blank to keep current value).")
            contact["name"] = input(f"Enter new name ({contact['name']}): ") or contact["name"]
            contact["phone"] = input(f"Enter new phone number ({contact['phone']}): ") or contact["phone"]
            contact["email"] = input(f"Enter new email address ({contact['email']}): ") or contact["email"]
            contact["address"] = input(f"Enter new address ({contact['address']}): ") or contact["address"]
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter the name or phone number of the contact to delete: ")
    for contact in contacts:
        if search_term == contact["name"] or search_term == contact["phone"]:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Main program
def main():
    print("Welcome to the Contact Book!")
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
main()
