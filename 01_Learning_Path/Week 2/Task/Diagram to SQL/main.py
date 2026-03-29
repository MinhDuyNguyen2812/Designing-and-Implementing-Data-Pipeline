import sqlite3

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    name = input("Enter your name: ")

    conn = sqlite3.connect("Students_Courses.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO logins (username, password, name) VALUES (?, ?, ?)",
            (username, password, name)
        )
        conn.commit()
        return "Register success"
    except:
        return "Username already exists"
    finally:
        conn.close()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    conn = sqlite3.connect("Students_Courses.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM logins WHERE username = ? AND password = ?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        print(f"Login success! Welcome {username}")
    else:
        print("Invalid username or password")

while True:
    choice = input("Choose option (register/login/exit): ").lower()
    if choice == "register":
        register()
    elif choice == "login":
        login()
    elif choice == "exit":
        break
    else:
        print("Invalid option")