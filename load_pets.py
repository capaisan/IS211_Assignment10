import sqlite3

conn = sqlite3.connect('pets.db')
cur = conn.cursor()

cur.execute("SELECT * FROM person")
rows_person = cur.fetchall()

cur.execute("SELECT * FROM pet")
rows_pet = cur.fetchall()

cur.execute("SELECT * FROM person_pet")
rows_person_pet = cur.fetchall()

print("People:")
for row in rows_person:
    print(row)

print("\nPets:")
for row in rows_pet:
    print(row)

print("\nPeople-Pets:")
for row in rows_person_pet:
    print(row)

conn.close()