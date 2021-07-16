from flask import Flask
from flask import render_template, request, redirect, url_for
from dao_movie import *
from movie_ins import *
import json
import sqlite3

app = Flask(__name__)


@app.route('/movie', methods=['GET', 'POST'])
def get_movie():
    conn = sqlite3.connect('movies.db')

    if request.method == 'GET':
        results = get_all_movies(conn)

        json_list = []
        for e in results:
            json_list.append(json.dumps(e.__dict__))
        return json.dumps(json_list)

    if request.method == 'POST':
        print(request.get_json())
        obj = request.get_json()
        e = MovieIns(obj['title'], obj['release_year'], obj['ticket_price'], obj['stars_rating'])
        insert_new_movie(conn, e)
        return 'success'


@app.route('/movie/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def movie_by_id(id):
    conn = sqlite3.connect('movies.db')

    if request.method == 'GET':
        result = get_movie_by_id(conn, id)
        return json.dumps(result.__dict__)

    if request.method == 'DELETE':
        delete_movie_by_id(conn, id)
        return 'success'

    if request.method == 'PUT':
        obj = request.get_json()
        e = MovieIns(obj['title'], obj['release_year'], obj['ticket_price'], obj['stars_rating'])
        update_movie_by_id(conn, e, id)
        return 'success'

app.run()