import mysql.connector
from keys.passwd import PASSWD

def refresh_database():

    # Here we are authenticating our connection to the MySQL database
    db = mysql.connector.connect(

        # The database I am using is with MySQL and it is a local database attached to the
        # user 'root'.
        host = "localhost",
        user = "root",

        # The password to the database is stored within a separate file for security.
        passwd = PASSWD,

        # Because I have already created the music database, we are able to connect to it here
        database = "music"
        )

    # A cursor to traverse the database and perform different actions within the database.
    my_cursor = db.cursor()

    # Query to create the database if it does not already exist.
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS music")

    # Drops (or Deletes) the table if it already exists.
    my_cursor.execute("DROP TABLE IF EXISTS Song")

    # Creates a new table for 'Song'
    my_cursor.execute("CREATE TABLE Song (songID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), genre VARCHAR(50), length smallint UNSIGNED)")

    # Inserts values into this new table 'Song'
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Clocks", "Alternative Rock", 307))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Bad Habit", "R&B/Soul", 232))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Have a Cigar", "Blues Rock", 267))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Hot Rod", "Pop", 197))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Im Yours", "Reggae", 242))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("The Color Violet", "R&B/Soul", 226))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("AMAZING", "Alternative/Indie", 209))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Pluto Projector", "Alternative/Indie", 267))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Fireflies", "Dance Electronic", 228))
    db.commit()

    # Returns the credentials and connection point to the database.
    return db

def describe(my_cursor):

    # Here, the DESCRIBE command is used to list the different data value names and their types
    # contained within the given table, which in this case is the 'Song' table.
    # These value names and types are then printed out to the terminal.
    my_cursor.execute("DESCRIBE Song")
    for x in my_cursor:
        print(x)

def query(my_cursor):

    # Using the SELECT command, we can select all columns from the 'Song' table
    # and then display all of the values from the table
    my_cursor.execute(f"SELECT * FROM Song")
    for x in my_cursor:
        print(x)

def alter(my_cursor):

    # Here we are able to add a new column to the table which is the artist.
    # This is done using the ALTER TABLE command.
    my_cursor.execute("ALTER TABLE Song ADD COLUMN artist VARCHAR(50)")

    # Here we are using the UPDATE command to set a new value to the artist column.
    # Using the WHERE command, you can set the artist to their specific songs by filtering them by name.
    my_cursor.execute("UPDATE Song SET artist = 'Coldplay' WHERE name = 'Clocks'")
    my_cursor.execute("UPDATE Song SET artist = 'Steve Lacy' WHERE name = 'Bad Habit'")
    my_cursor.execute("UPDATE Song SET artist = 'Pink Floyd' WHERE name = 'Have a Cigar'")
    my_cursor.execute("UPDATE Song SET artist = 'Dayglow' WHERE name = 'Hot Rod'")
    my_cursor.execute("UPDATE Song SET artist = 'Jason Mraz' WHERE name = 'Im Yours'")
    my_cursor.execute("UPDATE Song SET artist = 'Tory Lanez' WHERE name = 'The Color Violet'")
    my_cursor.execute("UPDATE Song SET artist = 'Rex Orange County' WHERE name = 'AMAZING' OR name = 'Pluto Projector'")
    my_cursor.execute("UPDATE Song SET artist = 'Owl City' WHERE name = 'Fireflies'")
    
def main():

    # Entry point of the code which controls the order of which the different operations occur.
    db = refresh_database()
    my_cursor = db.cursor()
    describe(my_cursor)
    alter(my_cursor)
    query(my_cursor)

if __name__ == "__main__":
    main()