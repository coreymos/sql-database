import mysql.connector
from keys.passwd import PASSWD

def refresh_database():
    # Here we are authenticated our connection to the SQL database
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = PASSWD,

        # Because I have already created the music database, we are able to connect to it here
        database = "music"
        )

    my_cursor = db.cursor()

    # Query to create the database if it does not already exist
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS music")

    # Drops table if it already exists
    my_cursor.execute("DROP TABLE IF EXISTS Song")

    # Creates a new table for 'Song'
    my_cursor.execute("CREATE TABLE Song (songID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), genre VARCHAR(50), length smallint UNSIGNED)")

    # Inserts values into this new table 'Song'
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Clocks", "Alternative Rock", 307))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Bad Habit", "R&B/Soul", 232))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Have a Cigar", "Blues Rock", 267))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Hot Rod", "Pop", 197))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("I'm Yours", "Reggae", 242))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("The Color Violet", "R&B/Soul", 226))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("AMAZING", "Alternative/Indie", 209))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Pluto Projector", "Alternative/Indie", 267))
    my_cursor.execute("INSERT INTO Song (name, genre, length) VALUES (%s, %s, %s)", ("Fireflies", "Dance Electronic", 228))
    db.commit()

    return db

def describe(my_cursor):
    my_cursor.execute("DESCRIBE Song")
    for x in my_cursor:
        print(x)

def query(my_cursor):
    my_cursor.execute("SELECT * FROM Song")
    for x in my_cursor:
        print(x)

def main():
    db = refresh_database()
    my_cursor = db.cursor()
    describe(my_cursor)
    query(my_cursor)

if __name__ == "__main__":
    main()