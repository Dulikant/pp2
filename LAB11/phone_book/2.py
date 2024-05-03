import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost', 
    dbname='dulatbasa', 
    user='postgres', 
    password='dulat2006',
    port='5432'
    )

# Create a cursor to work with the database
cur = conn.cursor()

import csv

filename = 'phone_data.csv'

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for row in csvreader:
        name, id, phone_number = row
        
        # Create new students
        cur.execute(f"""INSERT INTO phone_book (name, id, phone_number) VALUES 
                    ('{name}', '{id}', '{phone_number}');
        """)