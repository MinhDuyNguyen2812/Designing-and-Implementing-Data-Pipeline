from sqlite3.dbapi2 import connect

conn = connect("Customers_Orders.db")

conn.execute("PRAGMA foreign_keys = ON")

c = conn.cursor()

sql_create_customers = """
    CREATE TABLE IF NOT EXISTS customers(
        customer_num INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        city TEXT NOT NULL,
        age INTEGER NOT NULL
    );
"""
sql_create_orders = """
    CREATE TABLE IF NOT EXISTS orders(
        order_num INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_num INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        FOREIGN KEY (customer_num) REFERENCES customers(customer_num)
    );
"""

try:
    c.execute(sql_create_customers)
    c.execute(sql_create_orders)
    conn.commit()
except:
    print(f"Query error!")

while True:
    Choice = int(input("Insert data? (1-New customer, 2- Existing customer, 0-no): "))
    if Choice == 1:
        customer_name = input("Customer name: ")
        city = input("Customer city: ")
        try:
            age = int(input("Customer age: "))
        except ValueError:
            print("Invalid age. Please enter a number.")
            continue
        print(f"Data inserted successfully!\n")

        while True:
            add_order = int(input(f"Add an order for customer '{customer_name}'? (1-yes, 0-no): "))
            if add_order == 1:
                product_name = input("Product name: ")
                try:
                    c.execute("INSERT INTO orders(customer_num, product_name) VALUES(?, ?)", (customer_name, product_name))
                    conn.commit()
                except Exception as e:
                    print(f"Failed to insert order for '{customer_name}': {e}")
                print(f"Order for '{product_name}' inserted successfully!\n")
            elif add_order == 0:
                break
            else:
                print("Invalid choice.")

    elif Choice == 2:
        customer_name = input("Enter the customer name: ")