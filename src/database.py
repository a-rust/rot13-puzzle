from sqlalchemy import (create_engine, Table, Column,
                        Integer, String, DateTime)

# Prerequisites before running this python file:
#   - A Database Management System (ex: MySQL) must be installed and set up on the user's system, along with a user, password, port number, and database
#   - Additionally, a database connection must be running (ex/ SQLTools)


# Function to get user's input regarding their database management system information
#   -Need this to run code for this project using user's own database
def create_user_url() -> str:
    user_dbms = input('Enter Database Management System (ex/ mysql): ')
    user_name = input('Enter Username (ex/ root): ')
    password = input('Enter Password: ')
    database = input('Enter Database name (ex/ my_database): ')
    user_info = [user_dbms, user_name, password, database]
    user_url = user_info[0] + '://' + user_info[1] + ':' + \
        user_info[2] + '@localhost/' + user_info[3]
    print(user_url)
    return user_url


user_url = create_user_url()


# Function for creating a new engine on a local server
def create_user_engine(user_url: str):
    engine = create_engine(user_url)
    return engine


user_engine = create_user_engine(user_url)


# Function that tests connection to local database
def connect_to_local_database():
    try:
        connection = user_engine.connect()
        print('Connected to database successfully')
    except:
        print('Failed')


connect_to_local_database()
