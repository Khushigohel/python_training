''' You are managing the inventory of a bookstore. 
You need to create a Python program that allows you to 
add new books to the inventory and display the current 
inventory.

 Program should contain add_book function which 
ask user name of book and in second line quantity 
of book. Add it in inventory dictionary
■ display_inventory: Print all books currently in dict
■ update_book_quantity: input book_name and 
updated quantity and update in dictionary.
■ Application should keep running until user wants 
to exit
'''
class Book_Inventory:
    def __init__(self):
        self.inventory_store={}

    def add_book(self):
        try:
            book_name=input("Enter the book name:")
            quantity=int(input("How many quantity take to buy..."))
            self.inventory_store[book_name]=quantity
            print("\n Book Add Sucessfully....")
        except ValueError:
            print("Quantity must be a number. Please try again.")
            

    def display_book(self):
        if not  self.inventory_store:
            print("\n Book is Not Avaliable")
        else:
            print("Book_Name    quantity")
            print("-"*35)
            for book_name,quantity in self.inventory_store.items():
                print(book_name, " ", quantity)
                print("\n ")

    def update_book_quantity(self):
        book_name=input("Enter the book name to update the quantity:")
        if book_name in self.inventory_store:
            quantity_update=int(input("How many quantity take to update..."))
            self.inventory_store[book_name]=quantity_update
            print("Book quantity updated successfully.\n")
        else:
            print("\n Book not found in inventory.")
        
Inventory_system=Book_Inventory()

while True:
    print("Book Invetory Management:")
    print("\n 1. Add the Book")
    print("\n 2. Display the Book")
    print("\n 3. Update the Book Quantity")
    print("\n 4. Exit")
        
    choice=int(input("\n Enter the choice:"))
    if choice == 1:
        Inventory_system.add_book()
    elif choice == 2:
        Inventory_system.display_book()
    elif choice == 3:
        Inventory_system.update_book_quantity()
    elif choice == 4:
        exit()
    else:
        print("Invalid choice....")