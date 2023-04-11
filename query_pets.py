import sqlite3

conn = sqlite3.connect('pets.db')

while True:
    person_id = int(input('Enter a person\'s ID (enter -1 to exit): '))

    if person_id == -1:
        break

    person_query = f'SELECT first_name, last_name, age FROM person WHERE id={person_id}'
    person_info = conn.execute(person_query).fetchone()

    if person_info is None:
        print('Error: person does not exist.')
        continue

    print(f'{person_info[0]} {person_info[1]}, {person_info[2]} years old')

    pet_query = f'SELECT name, breed, age, dead FROM pet JOIN person_pet ON pet.id=person_pet.pet_id WHERE person_id={person_id}'
    pets_info = conn.execute(pet_query).fetchall()

    if len(pets_info) == 0:
        print('This person has no pets.')
    else:
        print('This person owned the following pets:')
        for pet_info in pets_info:
            pet_name = pet_info[0]
            pet_breed = pet_info[1]
            pet_age = pet_info[2]
            pet_dead = pet_info[3]

            if pet_dead == 1:
                print(f'{pet_name}, a {pet_breed}, that lived for {pet_age} years.')
            else:
                print(f'{pet_name}, a {pet_breed}, that is {pet_age} years old.')-