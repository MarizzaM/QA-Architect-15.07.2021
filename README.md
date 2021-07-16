# QA-Architect-15.07.2021
REST api with sqlite, flask / Python

create a new table in the db called movies with fileds: id (primary-key, auto-increment), title (text), release_year (int), ticket_price (real), stars_rating (int)
insert few movies into the table
create a Movie class with __init__ (self, id, title, release_year, ticket_price, stars_rating)
create a DAO for the table, make sure you get the conn as a parameter (like we did in class, see example above)
create a REST api with flask that exposes: get, get_by_id, post, put, delete (like we did in class, see example above)
test the REST api using postman
