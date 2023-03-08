# Project Description
This is a more in-depth page keeping track of my philosophy, outline about the project the project. I also give some design remarks, and some reflections about the process as I work through each step.

# Table of Contents
- [Project Description](#project-description)
- [Table of Contents](#table-of-contents)
  - [Philosophy](#philosophy)
  - [Outline](#outline)
  - [Remarks](#remarks)
  - [Project Structure](#project-structure)
  - [Reflections](#reflections)
    - [Step 1](#step-1)
  - [Step 2](#step-2)
  - [Step 3](#step-3)
  - [Step 4](#step-4)


## Philosophy
The goal of this project is to apply what I have learned regarding:
* MySQL, the relational database management system
* SQLAlchemy, the object-relational mapping
* Unit testing (this idea was first introduced to me when learning Rust, and I now want to apply it using Python)
  * Will be using the Pytest package

I would also like this project to be simple and interactive.

## Outline

1. Generate a random 5-letter string, and encrypt it using the [ROT13 cipher](https://en.wikipedia.org/wiki/ROT13)
2. User is given the ciphertext
   * Non-deterministic (i.e., each user is given a random string, and thus a random ciphertext)
3. Users are asked to submit an alias (an identifier), along with the decrypted plaintext
   * The alias will be a string, and the decrypted plaintext will be a string, but will map to $x\in{\{0,1\}}$ (either for being the correct or incorrect plaintext)
4. The results will be stored in a local database
   * 3 columns; alias, plaintext, truth_value
   * No interaction with remote database
5. The database will be queried to gather the number of correct and incorrect answers, and will display each in a histogram

## Remarks

* The choice of 5-letter strings (and thus ciphertexts) is arbitrary
* The alias identifier is not unique, which isn't a huge problem in this low-stakes demo
  * However, if this were a competition, someone could submit a fake alias and an incorrect plaintext
* Step 5 in the outline is also arbitrary, and may change
  * The idea is to do something with the data involving queries
* There is no remote database
  * Each user will create there own database, and interact with it using this code

## Project Structure
1. Branch for generating random plaintext strings
2. Branch for implementing ROT13 algorithm
3. Branch for using SQLAlchemy to create a database and table with the specified columns
4. Branch for importing user input into the database
5. Branch for querying data for truth_values, and displaying it


## Reflections

### Step 1
Making the function for randomly generating 5 letter strings was easy.  

I decided to include unit tests to make sure my function (and future functionalities) are working properly
* So I looked into the Pytest module  

Using Pytest requires creating test_<file_name> files for the functionality of <file_name>.py
* I wanted to keep these tests in a separate directory

However, importing <file_name> into test_<file_name> was very confusing
* Coming from Rust, I expected the module system to be pretty straight-forward
* After a lot of research, I managed to figure things out

Actually writing the unit test was pretty neat and simple (especially with the assert syntax, which I was used to in Rust)
* I could have easily defined a single function in ./src/plaintext.py to both generate the random list, and then convert it into a string, but I wanted to separate them to get a feel for how unit testing works in Python

## Step 2
Implementing ROT13 was straight-forward, and so was the unit test to check each edge case.

I realized that importing a module that imported another module was causing problems
* The fix was to just use the same boilerplate code when importing any module into any other module
  * I feel like I may be doing things wrong, so I'll have to look into other (successful) ways of importing external directory modules

## Step 3
I'm realizing that a remote server for the database may have been a better idea
* That way, users could interact with an existing database instead of creating their own, which has many prerequisites

Creating the local table within an existing database was pretty straight-forward (at least after learning more about SQLAlchemy)
* Next step will involve actually filling in the table using user input

## Step 4
Because Python is so confusing when it comes to external directory imports, I refactored my code
* I combined plaintext.py and ciphertext.py into a single python file, rot13.py
* I combined test_plaintext.py and test_ciphertext.py into a single python test file, test_rot13.py
* Everything seemed to work much smoother, and I didn't have to resort to obscure import methods

Implementing the function that creates puzzles involved appending lists inside of a larger list, and handling user input, which wasn't too complicated.

So far, we have implemented a program that:
* Connects to the user's SQL Database Management System
* Creates an empty table
* Imports data using rot13 puzzles

To finish the project, I would like to interact with database table by making some queries, and displaying the results in an interesting way.