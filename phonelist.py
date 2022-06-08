#import sqlite3
#conn = sqlite3.connect("phone.db")
import psycopg2
conn = psycopg2.connect(
           host="localhost",
           database="phone",
           user="phone",
           password="abc123"
       )


print("-----Hello and welcome to the phonelist-----")

commands = [
    'ADD: Add a name, number and address to the list',
    'LIST: Print the list of names',
    'DELETE: Delete a name from the list',
    'SAVE: Save the phonelist to database',
    'QUIT: End the program']
for x in commands:
    print(x)

def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
    print("Phone added")
def delete_phone(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id}';")
    cur.close()
    print("Phone deleted")
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
        address = input(" Address: ").strip().upper()
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":       
        id = input("  Id: ").strip()
        delete_phone(conn, id)
    elif cmd == "QUIT":
        save_phonelist(conn)
        exit()
    elif cmd == "SAVEd":
        save_phonelist(conn)
        print("Saved")
    elif cmd == "HELP":
        for x in commands:
            print(x)
    else:
        print("Please use a valid command")
        for x in commands:
            print(x)