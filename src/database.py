from sqlalchemy import (create_engine, Table, Column,
                        Integer, String, DateTime)
from sqlalchemy.orm import sessionmaker, declarative_base
from user_input import create_puzzles
import plotext


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
    print('')
    print("Let's test your rot13 decryption skills ... ")
    print('')
    return user_url


user_url = create_user_url()


# Function for creating a new engine on a local server
def create_user_engine(user_url: str):
    engine = create_engine(user_url)
    return engine


user_engine = create_user_engine(user_url)


# Creating a new user session with the database
Session = sessionmaker(bind=user_engine)
user_session = Session()

# Declaring the base class for our Rot13 class
Base = declarative_base()


# Class which contains our table
#  - 'id' is unique (to identify each puzzle)
#  - 'ciphertext' is the encrypted plaintext using rot13
#  - 'plaintext' is the randomly generated 5-letter string
#  - 'answer' will be whether the plaintext is the decryption of the ciphertext
#
# Note that if 'Rot13' already exists, no new table will be created, and the functions that insert rows into the table will insert them into the original table named 'Rot13_test2'
class Rot13(Base):
    __tablename__ = 'Rot13'
    id = Column(Integer, primary_key=True)
    ciphertext = Column(String(3))
    plaintext = Column(String(3))
    answer = Column(Integer)


# Creating the (empty) table in our database
Base.metadata.create_all(user_engine)


# Function to enter in data user submitted from puzzles
def enter_data_into_table(database_entries: list[list, list, list]):
    for puzzle in range(0, len(database_entries[0])):
        puzzle_entry = Rot13(
            ciphertext=database_entries[0][puzzle], plaintext=database_entries[1][puzzle], answer=database_entries[2][puzzle])
        user_session.add(puzzle_entry)
        user_session.commit()


enter_data_into_table(create_puzzles())


# Function for displaying correct vs incorrect totals through a histogram
def get_totals() -> list[int]:
    # Set up query into the Rot13 table
    puzzles = user_session.query(Rot13)
    correct_count = 0
    incorrect_count = 0
    for puzzle in puzzles:
        if puzzle.answer == 1:
            correct_count += 1
        else:
            incorrect_count += 1
    totals = [correct_count, incorrect_count]
    return totals


# Function for displaying statistics in the terminal
def statistics(totals: list):
    plotext.simple_bar(['Correct', 'Incorrect'], totals,
                       width=100, title='Correct vs Incorrect Decryptions')
    plotext.show()


statistics(get_totals())
