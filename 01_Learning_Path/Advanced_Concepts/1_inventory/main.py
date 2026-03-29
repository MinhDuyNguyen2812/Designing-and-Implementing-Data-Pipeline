from file_handler import FileHandler

filename = "inventory.csv"
inventory_file = FileHandler(filename)
rows = inventory_file.read()
print(f"#####Start {filename} #####")
for row in rows:
    print(row)
print(f"#####End: {filename} #####")