from movie import *


def create_movie_table(conn):
    conn.execute('''
        CREATE TABLE MOVIE
        (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
        TITLE TEXT NOT NULL, RELEASE_YEAR INT NOT NULL,
        TICKET_PRICE REAL, STARS_RATING INT NOT NULL)
        ''')


def insert_new_movie(conn, e):
    conn.execute(f'''
    INSERT INTO MOVIE
    (TITLE, RELEASE_YEAR, TICKET_PRICE, STARS_RATING)
    VALUES
    ('{e.title}', {e.release_year}, {e.ticket_price}, {e.stars_rating})''')
    conn.commit()

    print("success")


def get_all_movies(conn):
    result = conn.execute('SELECT * FROM MOVIE')
    movie_list = []
    for row in result:
        e = Movie(row[0], row[1], row[2], row[3], row[4])
        movie_list.append(e)
    return movie_list


def get_movie_by_id(conn, id):
    result = conn.execute(f'SELECT * FROM MOVIE WHERE ID = {id}')
    for row in result:
        e = Movie(row[0], row[1], row[2], row[3], row[4])
        return e
    return None


def update_movie_by_id(conn, e, id):
    conn.execute(f'''UPDATE MOVIE SET
    TITLE = '{e.title}', RELEASE_YEAR = {e.release_year}, 
    TICKET_PRICE = {e.ticket_price}, STARS_RATING = {e.stars_rating}
    WHERE ID = {id}''')
    conn.commit()


def delete_movie_by_id(conn, id):
    conn.execute(f'DELETE FROM MOVIE WHERE ID = {id}')
    conn.commit()

