from sqlite3.dbapi2 import connect

conn = connect("Books_Authors.db")

conn.execute("PRAGMA foreign_keys = ON")

c = conn.cursor()

sql_create_authors = """
    CREATE TABLE IF NOT EXISTS authors(
        author_name TEXT PRIMARY KEY,
        country TEXT NOT NULL
    );
"""
sql_create_books = """
    CREATE TABLE IF NOT EXISTS books(
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_name TEXT NOT NULL,
        title VARCHAR(255) NOT NULL,
        FOREIGN KEY (author_name) REFERENCES authors(author_name)
    );
"""

try:
    c.execute(sql_create_authors)
    c.execute(sql_create_books)
    conn.commit()
except:
    print(f"Query error!")

while True:
    Choice = int(input("Insert data? (1-New author, 2-Existing author, 0-no): "))
    if Choice == 1:
        author_name = input("Author name: ")
        country = input("Author country: ")
        try:
            c.execute("INSERT INTO authors(author_name, country) VALUES(?, ?)", (author_name, country))
            conn.commit()
        except Exception as e:
            print(f"Failed to insert author '{author_name}': {e}")
            continue
        print("Data inserted successfully!\n")

        while True:
            add_book = int(input(f"Add a book for author '{author_name}'? (1-yes, 0-no): "))
            if add_book == 1:
                title = input("Book title: ")
                try:
                    c.execute("INSERT INTO books(author_name, title) VALUES(?, ?)", (author_name, title))
                    conn.commit()
                    print(f"Book '{title}' inserted successfully!\n")
                except Exception as e:
                    print(f"Failed to insert book '{title}': {e}")
            elif add_book == 0:
                break
            else:
                print("Invalid choice.")

    elif Choice == 2:
        author_name = input("Enter the author name: ")
        title = input("Book title: ")
        try:
            c.execute("INSERT INTO books(author_name,title) VALUES(?, ?)", (author_name, title))
            conn.commit()
            print(f"Book '{title}' inserted successfully!\n")
        except Exception as e:
            print(f"Failed to insert book '{title}': {e}")

    elif Choice == 0:
        break
    else:
        print("Invalid choice.")


conn.close()