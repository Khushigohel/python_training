''' Develop a Python program to manage a contact book.
● Allow users to add new contacts, search for contacts by name, and delete contacts.
● Use a dictionary to store contacts where the keys are contact names and the values are 
dictionaries containing contact information like phone number, email, etc.
● Implement error handling for cases where a contact is not found during search or 
deletion.'''

class Contact_Book:
    def __init__(self):
        self.contact_book={}
    
    def add_contact(self):
        Name=input("Enter the Contact Name: ")
        Phone_no=input("Enter the Contact Number: ")
        Email=input("Enter the Email: ")
        
        self.contact_book[Name]={
            'Phone_number':Phone_no,
            'Email':Email
        }
        print("\n Contact Add Sucessfully...")
    
    def display_contact(self):
        print("========== Contact Informaion ========")
        if not self.contact_book:
            print("\n No Contact Save....")
        for name,details in self.contact_book.items():
            print(f"{name} → Phone: {details['Phone_number']} | Email: {details['Email']}")
        print()
    
    def search_conact(self):
        Name=input("Enter the Contact Name: ")
        try:
            print("-"*50)
            print(" \n Search for contacts by name Below")
            contact=self.contact_book[Name]
            print(f" \n Name : {Name}")
            print(f" \n Phone Number : {contact['Phone_number']}")
            print(f" \n Email of the : {contact['Email']}")
            print("-"*50)
        except KeyError:
              print(f"\nError: Contact '{Name}' not found!\n")
    
    def delete_contact(self):
        Name=input("Enter the Contact Name: ").strip()
        try:
            if Name not in self.contact_book:
                print("\n THis Name is Not Avaliable in Dictonary sorry....")
            del self.contact_book[Name]
            print(f"\nContact '{Name}' deleted successfully!\n")
        except:
            print(f"\nError: Contact '{Name}' not found!\n")
    
    def menu(self):
        while True:
            print("\n Welcome Users...")
            print("\n 1. Add the Contact")
            print("\n 2. Dispaly the Contact")
            print("\n 3. Search the Contact ")
            print("\n 4. Remove Contact")
            print("\n 5.Exit")
            
            choice=int(input("\nEnter the Choice:"))
            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.display_contact()
            elif choice == 3:
                self.search_conact()
            elif choice == 4:
                self.delete_contact()
            else:
                exit()

contact_book=Contact_Book()
contact_book.menu()

    
    