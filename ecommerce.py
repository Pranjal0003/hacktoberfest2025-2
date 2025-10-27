import pandas as pd

inventory = {
    'Electronics': [],
    'Clothing': [],
    'Groceries': []
}

# inventory=pd.DataFrame(data=inventory_1)

# def display_menu():
print("1. Add Product")
print("2. View Products")
print("3. Update Product")
print("4. Delete Product")
print("5. Show Summary")
print("6. Search Product")
print("7. Exit")

def menu_record():
    for choice in range(1,7):
        choice=input("Enter your choice: ")
        if choice=='1':
            insert()
        elif choice=='2':
            view()
        elif choice=='3':
            update()
        elif choice=='4':
            delete()
        elif choice=='5':
            summary()
        elif choice=='6':
            exit
        else:
            print("Invalid choice ! please enter valid choice")


            

def insert():
    try:
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        category = input("Enter product category (Electronics/Clothing/Groceries): ")
        if category not in inventory:
            print("Invalid category!")
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))
        supplier = input("Enter supplier name: ")
        
        product = {
            'product_id': product_id,
            'name': name,
            'category': category,
            'quantity': quantity,
            'price': price,
            'supplier': supplier
        }

        inventory[category].append(product)
        print("Product added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def view():
    for category in inventory:
        print(f"\nCategory: {category}")
        for product in inventory[category]:
            print(product)
    print("\n")

def update():
    try:
        category = input("Enter product category to update (Electronics/Clothing/Groceries): ")
        if category not in inventory:
            print("Invalid category!")
        product_id = input("Enter product ID to update: ")
        for product in inventory[category]:
            if product['product_id'] == product_id:
                product['name'] = input("Enter new product name: ")
                product['quantity'] = int(input("Enter new product quantity: "))
                product['price'] = float(input("Enter new product price: "))
                product['supplier'] = input("Enter new supplier name: ")
                print("Product updated successfully!")
                return
        print("Product not found!")
    except ValueError as e:
        print(f"Error: {e}")

def delete():
    try:
        category = input("Enter product category to delete (Electronics/Clothing/Groceries): ")
        if category not in inventory:
            print("Invalid category!")
        product_id = input("Enter product ID to delete: ")
        for product in inventory[category]:
            if product['product_id'] == product_id:
                inventory[category].remove(product)
                print("Product deleted successfully!")
                return
        print("Product not found!")
    except ValueError as e:
        print(f"Error: {e}")

def summary():
    total_value = 0
    for category in inventory:
        category_value = sum(product['price'] * product['quantity'] for product in inventory[category])
        total_value += category_value
        avg_price = category_value / len(inventory[category]) if inventory[category] else 0
        print(f"Category: {category}")
        print(f"Total Value: {category_value}")
        print(f"Average Price: {avg_price}")

    print(f"Total inventory value: {total_value}")
    
    # Top-selling products and reorder alerts
    low_stock_threshold = 10  # Example threshold
    for category in inventory:
        print(f"\nReorder Alerts for {category}:")
        for product in inventory[category]:
            if product['quantity'] <= low_stock_threshold:
                print(f"Low stock alert: {product['name']} (ID: {product['product_id']})")




menu_record()
