from sqlite3.dbapi2 import connect

conn = connect("Students_Courses.db")

conn.execute("PRAGMA foreign_keys = ON")

c = conn.cursor()

sql_create_task = """
    CREATE TABLE IF NOT EXISTS task (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
        );
"""
sql_create_course_assignment = """
    CREATE TABLE IF NOT EXISTS course_assignment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_task INTEGER NOT NULL,
        id_course INTEGER NOT NULL
    );
"""
sql_create_course = """
    CREATE TABLE IF NOT EXISTS course (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
        );
"""
sql_create_credits = """
    CREATE TABLE IF NOT EXISTS credits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_course INTEGER NOT NULL,
        id_student INTEGER NOT NULL,
        date TEXT NOT NULL,
        grade TEXT NOT NULL,
        credits INTEGER NOT NULL,
        FOREIGN KEY (id_course) REFERENCES course_assignment(id_course)
    );
"""
sql_create_student = """
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL,
        major TEXT NOT NULL
    );
"""
sql_create_task_completion = """
    CREATE TABLE IF NOT EXISTS task_completion (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_task INTEGER NOT NULL,
        id_student INTEGER NOT NULL,
        time TEXT NOT NULL,
        FOREIGN KEY (id_task) REFERENCES course_assignment(id_task),
        FOREIGN KEY (id_student) REFERENCES credits(id_student)
    );
"""

try:
    c.execute(sql_create_task)
    c.execute(sql_create_course_assignment)
    c.execute(sql_create_course)
    c.execute(sql_create_credits)
    c.execute(sql_create_student)
    c.execute(sql_create_task_completion)
    conn.commit()
except:
    print(f"Query error!")

conn.close()