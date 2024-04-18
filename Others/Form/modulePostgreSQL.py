import psycopg2
import json

# Define database credentials at the module level
json_filepath = r'D:\Repos\scriptsPython\Others\Form\credentials.json'

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

db_user, db_password, db_name, db_host, db_port = load_credentials(json_filepath)

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

def insert_record(name, country, population, area):
    try:
        conn = db_connection(db_user, db_password, db_name, db_host, db_port)
        if conn:
            cur = conn.cursor()
            insert_query = "INSERT INTO cities (name, country, population, area) VALUES (%s, %s, %s, %s)"
            cur.execute(insert_query, (name, country, population, area))
            conn.commit()
            return True
        else:
            return False
    except psycopg2.Error as e:
        print("Error inserting record:", e)
        return False
    finally:
        if conn:
            cur.close()
            conn.close()
