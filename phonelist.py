#import sqlite3
#conn = sqlite3.connect("phone.db")
import psycopg2
conn = psycopg2.connect(
           host="localhost",
           database="phone",
           user="phone",
           password="abc123"
       )

the_list = []
print("-----Hello and welcome to the phonelist-----")

commands = [
    'ADD: Add a name to the list',
    'LIST: Print the list of names',
    'DELETE: Delete a name from the list',
    'QUIT: End the program']
for x in commands:
    print(x)

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
    print("phone deleted")
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
    except:
        print("No changes!")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ").strip().title()
        phone = input("  Phone: ").strip().title()
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ").strip().title()
        delete_phone(conn, name)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
