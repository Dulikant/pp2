
import psycopg2

# Function to get all contacts
def get_all_contacts():
    conn = psycopg2.connect("dbname=dulatbasa user=postgres password=dulat2006 port=5432")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_book")
    rows = cur.fetchall()
    
    conn.close()
    
    return rows

# Function to search contacts by first name
def search_by_first_name(name):
    conn = psycopg2.connect("dbname=dulatbasa user=postgres password=dulat2006 port=5432")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_book WHERE name = %s", (name,))
    rows = cur.fetchall()
    
    conn.close()
    
    return rows

# Function to search contacts by phone number
def search_by_phone(phone_number):
    conn = psycopg2.connect("dbname=lab10 user=postgres password=Aldiyar2005@ port=5433")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM phone_book WHERE phone_number = %s", (phone_number,))
    rows = cur.fetchall()
    
    conn.close()
    
    return rows



if __name__ == "__main__":
    # Example usage
    contacts = get_all_contacts()
    print("All Contacts:")
    for contact in contacts:
        print(contact)

    nurlybek = search_by_first_name("Nurlybek")
    print("\nContacts with first name 'Nurlybek':")
    for contact in nurlybek:
        print(contact)

    number = "+77029572379 "
    contact_by_phone = search_by_phone(number)
    print(f"\nContact with phone number {number}:")
    print(contact_by_phone)

    '''# Deleting a contact by username
    delete_contact_by_username("Mikel")
    print("\nDeleted contact with first name 'Mikel'")
    
    # Get all contacts again after deletion
    remaining_contacts = get_all_contacts()
    print("\nRemaining Contacts:")
    for contact in remaining_contacts:
        print(contact)'''