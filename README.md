# Overview

This is an Inventory Management Program. This program keeps track of the quantity, name and price of the items of a company and saves them to a database named Inventory. The program has the function to add and delete an item from the database, and 2 other functions to sell and restock the items. The last two functions substract and add quantities to the items in the database respectively, and the sale function shows the revenue made with the sale.

I made this program to understand the basics of SQL Relational Databases,and to demonstrate how to use SQLite with Python with the sqlite3 library.

[Software Demo Video](https://youtu.be/Ekupuy1eeAs)

# Relational Database

I used SQLite to create a database with a table named inventory that consists on 4 fields. An ID field which is an integer and the primary key, a text type field named Name, an integer field named Quantity, and a real number field named Price.

# Development Environment

- VS Code
- Python 3.10.7 (64-bit)
- sqlite3 library

# Useful Websites

- [Python SQLite3 documentation](https://docs.python.org/3.8/library/sqlite3.html)
- [SQLite Python Tutorial site](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

# Future Work

- I want to create another table to keep track of the sales
- I also want to add a function that prints a receipt for each sale