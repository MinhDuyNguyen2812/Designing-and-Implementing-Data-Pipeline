from sqlite3.dbapi2 import connect

conn = connect("Create_Table.db")

c = conn.cursor()

sql_create_table = """
    CREATE TABLE account(
        account_id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_name VARCHAR(255) NOT NULL,
        balance NUMBER NOT NULL,
        city TEXT NOT NULL
    );
"""
sql_insert = """
    INSERT INTO account VALUES(NULL, 'Jane', 123000.12, 'Lappeenranta');
"""
sql_select = """
    SELECT * FROM account LIMIT 1;
"""
sql_update = """
    UPDATE account SET balance = 520 WHERE account_id = 1;
"""
sql_delete = """
    DELETE FROM account WHERE balance < 1000
"""
try:
    c.execute(sql_delete)
    conn.commit()
    c.execute(sql_select)
    print(c.fetchall())
    
except:
    print(f"Query error!")
conn.close()