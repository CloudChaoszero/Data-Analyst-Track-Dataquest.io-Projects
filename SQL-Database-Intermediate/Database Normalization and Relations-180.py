## 4. Querying a normalized database ##

import sqlite3 as sql
portman_movies = sql.connect('academy_awards.db').execute('SELECT cer.year, nom.movie FROM ceremonies as cer INNER JOIN nominations as nom ON cer.id = nom.ceremony_id WHERE nom.nominee=="Natalie Portman";').fetchall()

for p in portman_movies:
    print(p)

## 7. Join table ##

import sqlite3 as sql
conn = sql.connect("academy_awards.db")
five_join_tableq = 'SELECT * FROM movies_actors LIMIT 5;'
five_actorsq = 'SELECT * FROM actors LIMIT 5;'
five_moviesq = 'SELECT * FROM movies LIMIT 5;'
five_join_table  = conn.execute(five_join_table).fetchall()
five_actors = conn.execute(five_actors).fetchall()
five_movies = conn.execute(five_movies).fetchall()
for p in five_join_table :
    print(p)
for q in five_actors:
    print(q)
for r in five_movies:
    print(r)

## 9. Querying a many-to-many relation ##

q = '''
SELECT actors.actor,movies.movie FROM movies
INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
INNER JOIN actors ON movies_actors.actor_id == actors.id
WHERE movies.movie == "The King's Speech";
'''
kings_actors = conn.execute(q).fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

import sqlite3 as sql
conn = sql.connect('academy_awards.db')
natp_query = ('SELECT movies.movie, actors.actor FROM movies INNER JOIN movies_actors ON movies.id==movies_actors.movie_id INNER JOIN actors ON movies_actors.actor_id==actors.id WHERE actors.actor=="Natalie Portman";')
portman_joins = conn.execute(natp_query).fetchall()
for p in portman_joins:
    print(p)