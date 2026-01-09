''' Design a Python program to manage an inventory system for a small store.
● The inventory should consist of items with attributes like name, quantity, price, and 
category.
● Implement functionality to add new items, update existing items, remove items, and 
display the inventory.
● Allow users to search for items by name or category and display details of the matching 
items.
● Include features for checking the availability of items, adding items to a shopping cart, 
and generating a bill.
● Ensure the program handles errors gracefully, such as attempting to remove a non
existent item or adding a negative quantity.
● Implement a simple text-based user interface with a menu system for navigating different 
functionalities '''

class Inventory_system:
    def __init__(self):
        self.inventory={}
        self.cart={}
    
    def add_item(self):
        item_name=input("Enter the Item Name : ")
        category=input("Enter the Category of the Iem : ")
        price=int(input("Enter the item Price : "))
        quantity=int(input("Enter the item Quanity : "))
        
        self.inventory[item_name] = {
            'category' : category,
            'price' : price,
            'quantity' : quantity
        }
        
        print(" \n Item Add Sucessfully....")
    
    def Display_Item(self):
        if not self.inventory:
            print("\n No Item is Avaliable...Sorry ... Come into nex Day....")
        print("Item_Name  |  Category  | Price | Quantity")
        print("-"*50)
        for name,deails in self.inventory.items():
            print(f"{name}  {deails['category']} {deails['price']}  {deails['quantity']}")
        print()
    
    def update_item(self):
        self.Display_Item()
        item_name=input("Enter the Name : ")
        if item_name not in self.inventory:
            print(" \n No Item is Present...")
        try:
            price=int(input("Enter the item Price : "))
            quantity=int(input("Enter the item Quanity : "))
            
            if price < 0 and quantity < 0 : 
                raise ValueError
        except ValueError:
            print("\nInvalid quantity or price!\n")
            return
        self.inventory[item_name]['price'] = price
        self.inventory[item_name]['quantity'] = quantity
        print(f" \n Item {item_name} Updated Sucessfully...")
    
    def remove_item(self):
        self.Display_Item()
        item_name=input("Enter the Name : ")
        if item_name not in self.inventory:
            print(" \n No Item is Present...")
        del self.inventory[item_name]
        print(f"\n Item '{item_name}' deleted successfully!\n")
        
    def search_by_name(self):
        self.Display_Item()
        item_name=input("Enter the Name : ")
        try:
         
            print(" \n Search for Item by name Below")
            print("-"*50)
            item=self.inventory[item_name]
            print(f" \n Item Name : {item_name}")
            print(f" \n Category Name : {item['category']}")
            print(f" \n Item Price : {item['price']}")
            print(f" \n Item Quantity : {item['quantity']}")
            print("-"*50)
        except KeyError:
              print(f"\nError: Contact '{item_name}' not found!\n")
    
    def search_category(self):
        cat = input("Enter category to search: ")
        results = [i for i in self.inventory.values() if i['category'] == cat]
        if results:
            print("\n--- Items Matching Category ---")
            for i in results:
                print(f"{i['category']} | Qty: {i['quantity']} | Price: {i['price']}")
            print()
        else:
            print("\nNo items found in this category.\n")
            
    def check_availability(self):
        name = input("Enter item name: ")
        item = self.inventory.get(name)
        if item:
            print(f"\n{name} available, Qty: {item['quantity']}\n")
        else:
            print("\nItem not found!\n")
    
    def add_to_cart(self):
        name = input("Enter item name to buy: ")
        if name not in self.inventory:
            print("\nItem not found!\n")
            return
        try:
            qty = int(input("Enter quantity: "))
            if qty <= 0:
                raise ValueError
        except ValueError:
            print("\nInvalid quantity!\n")
            return
        item=self.inventory[name]
        if qty > item['quantity']:
            print("\nNot enough stock!\n")
            return
        item['quantity'] -= qty
        self.cart[name] = self.cart.get(name, 0) + qty
        print("\nItem added to cart!\n")
    
    def generating_bill(self):
        if not self.cart:
            print("\nCart is empty.\n")
            return
        total = 0
        print("\n--- Bill ---")
        for name, qty in self.cart.items():
            price = self.inventory[name]['price']
            amount = qty * price
            print(f"{name} | Qty: {qty} | Price: {price} | Amount: {amount}")
            total += amount

        print(f"\nTotal Amount: {total}\n")
        print("\n--- Thank You Visit Again ---")
        self.cart.clear()

obj=Inventory_system()

while True : 
    print("\n Welcome to Invemtory Store....")
    print(" \n 1. Add the Item")
    print(" \n 2. Display the Item")
    print(" \n 3. Update the Item")
    print(" \n 4. Remove the Item")
    print("\n 5. Search by Item Name")
    print("\n 6. search by Category Itme")
    print("\n 7. checking the availability of item")
    print("\n 8. Add to Cart")
    print("\n 9 Generate the bill")
    print(" \n 8. Exit")
    
    choice=int(input("Enter the Choice : "))
    
    if choice == 1:
        obj.add_item()
    elif choice == 2:
        obj.Display_Item()
    elif choice == 3:
        obj.update_item()
    elif choice == 4:
        obj.remove_item()
    elif choice == 5:
        obj.search_by_name()
    elif choice == 6:
        obj.search_category()
    elif choice == 7:
        obj.check_availability()
    elif choice == 8:
        obj.add_to_cart()
    elif choice == 9:
        obj.generating_bill()
    else:
        exit()
