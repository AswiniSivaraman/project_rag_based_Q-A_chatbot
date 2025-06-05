def drop_table_users(cursor):
    cursor.execute("drop table if exists users;")

def drop_table_comments(cursor):
    cursor.execute("drop table if exists comments;")


def drop_table_embedded_movies(cursor):
    cursor.execute("drop table if exists embedded_movies;")


def drop_table_movies(cursor):
    cursor.execute("drop table if exists movies;")


def drop_table_sessions(cursor):
    cursor.execute("drop table if exists sessions;")


def drop_table_theaters(cursor):
    cursor.execute("drop table if exists theaters;")