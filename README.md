# ROT13 Decryption Database
This was an educational project for me to learn and apply concepts involving standard query language (SQL), database management systems (DBMS), and object relational mappings (ORM).

## Project Description
This project:
* Builds a local database (table) using a DBMS (ex/ MySQL)
* Generates random [ROT13 decryption](https://en.wikipedia.org/wiki/ROT13) puzzles for the user to answer
* Inserts the answers into the database table
* Queries the table to determine puzzle accuracy
* Displays correct vs incorrect puzzle results

For more details regarding my experience building the project, check the [Project Description](https://github.com/a-rust/rot13-puzzle/blob/main/PROJECT_DESCRIPTION.md)

# Demo
![Rot13_summary](https://user-images.githubusercontent.com/107306810/223645491-4f5674e9-fa46-47ac-9e7c-e1914554a1c5.png)


---

![MySQL_table](https://user-images.githubusercontent.com/107306810/223645606-904a7eb6-5508-4750-8cdb-2f78c545cd58.png)


# Dependencies
* Python 3.11 or greater
* Relational Database Management System (ex/ MySQL, PostgreSQL, SQLite, etc.)
* Python packages:
  * SQLAchemy
  * Random
  * Plotext

# How to run this project yourself
1. Clone this repo:
```
git clone https://github.com/a-rust/rot13-puzzle.git
cd rot13_puzzle
```  
1. Load up a DBMS:
```
-- For example, using MySQL
mysql -u <user_name> -p
# Enter password  
```
1. Create a new database:
```
-- For example, using MySQL
CREATE DATABASE <database_name>
```
1. Run ./src/database.py:
```
python3 ./src/database.py
```
1. Interact with the terminal, and check your database for the full results in the table 'Rot13':
```
-- For example, using MySQL
SELECT * FROM Rot13_Puzzles
```
