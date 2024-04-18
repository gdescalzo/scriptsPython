import psycopg2
import json

# Load the credentials from a JSON file
def load_credentials(json_filepath):
    with open(json_filepath, 'r') as f:
        data = json.load(f)

    credentials = data['db_crendetials'][0]
    db_user = credentials['db_user']
    db_password = credentials['db_password']
    db_name = credentials['db_name']
    db_host = credentials['db_host']
    db_port = credentials['db_port']

    return db_user, db_password, db_name, db_host, db_port

def db_connection(db_user, db_password, db_name, db_host, db_port):
    try:
        conn = psycopg2.connect(
            host=db_host,
            dbname=db_name,
            user=db_user,
            password=db_password,
            port=db_port
        )
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database:", e)
        return None

# Use the function to load credentials:
json_filepath = r'D:\Repos\scriptsPython\Others\Form\credentials.json'
db_user, db_password, db_name, db_host, db_port = load_credentials(json_filepath)

# Queries
postgres_query = 'SELECT * FROM cities;'

# Establish the connection
conn = db_connection(db_user, db_password, db_name, db_host, db_port)
if conn:
    print("Connection established successfully!")
    cur = conn.cursor()
    cur.execute(postgres_query)
    
    # Fetch all rows from the result set
    rows = cur.fetchall()
    
    # Print the rows
    for row in rows:
        print(row)
    
    conn.commit
    
    cur.close
    conn.close
    
else:
    print("Failed to establish connection.")