# Overview

This program is a demonstration of my intro to SQL and connecting it to a python program. SQL relational databases are very commonly used by companies to store data. So it is important that I go through this hands-on process of using SQL and python together so that I am familiar with how it works.

[Software Demo Video](https://youtu.be/0D8-DB8M42g)

# Relational Database

I am using MySQL Workbench with one table labeled 'Song'.

The 'Song' table contains the following values:
* songID int AI PK 
* name varchar(50) 
* genre varchar(50) 
* length smallint UN
* artist varchar(50)

# Development Environment

* MySQL Workbench
* Python 3.11
* Python SQL Connector (Library)
* Github
* Visual Studio Code

# Useful Websites

- [YouTube - Channel: Tech with Tim / Title: Python MySQL Tutorial](https://www.youtube.com/watch?v=91iNR0eG8kE)
- [W3 Schools](https://www.w3schools.com/sql/)

# Future Work

- Add an interface to allow the user to interact with the database from outside the code
- Add more tables and relate them to each other (Genre Table, Artist Table, etc.)
- Use SELECT and WHERE queries in order to select only specific data from the table or tables