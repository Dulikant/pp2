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

conn.commit() 

cur.execute("""DELETE FROM phone_book
            WHERE id = '010101';
""")

