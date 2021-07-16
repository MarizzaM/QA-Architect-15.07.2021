import sqlite3

conn = sqlite3.connect('movies.db')


def create_movie_table():
    conn.execute('''
        CREATE TABLE MOVIE
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        TITLE TEXT NOT NULL, RELEASE_YEAR INT NOT NULL,
        TICKET_PRICE REAL, STARS_RATING INT NOT NULL)
        ''')


def insert_into_movie_table():
    conn.execute('''
    INSERT INTO MOVIE
    (TITLE, RELEASE_YEAR, TICKET_PRICE, STARS_RATING)
    VALUES
    ('Black Widow', 2021, 59.9, 6)
    ''')
    conn.execute('''
    INSERT INTO MOVIE
    (TITLE, RELEASE_YEAR, TICKET_PRICE, STARS_RATING)
    VALUES
    ('Shang-Chi and the Legend of the Ten Rings', 2021, 49.9, 9)
    ''')
    conn.execute('''
    INSERT INTO MOVIE
    (TITLE, RELEASE_YEAR, TICKET_PRICE, STARS_RATING)
    VALUES
    ('Eternals', 2021, 69.9, 9)
    ''')
    conn.commit()

    print("success")


def drop_movie_table():
    conn.execute("DROP TABLE MOVIE;")
    conn.commit()


def print_movie_table():
    result = conn.execute('SELECT * FROM MOVIE')
    for row in result:
        print("ID = ", row[0])
        print("TITLE = ", row[1])
        print("RELEASE_YEAR = ", row[2])
        print("TICKET_PRICE = ", row[3])
        print("STARS_RATING = ", row[4])
        print("=========================")


def update_movie_by_id():
    conn.execute("UPDATE MOVIE SET STARS_RATING = 8 WHERE ID = 1")
    conn.commit()


def delete_movie_by_id():
    conn.execute("DELETE FROM MOVIE WHERE ID = 1")
    conn.commit()


create_movie_table()
insert_into_movie_table()
print_movie_table()
update_movie_by_id()
print_movie_table()
delete_movie_by_id()
print_movie_table()
# drop_movie_table()
