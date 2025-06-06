def drop_table_users(cursor):
    """
    Drops the 'users' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'users' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists users;")

def drop_table_comments(cursor):
    """
    Drops the 'comments' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'comments' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists comments;")


def drop_table_embedded_movies(cursor):
    """
    Drops the 'embedded_movies' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'embedded_movies' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists embedded_movies;")


def drop_table_movies(cursor):
    """
    Drops the 'movies' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'movies' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists movies;")


def drop_table_sessions(cursor):
    """
    Drops the 'sessions' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'sessions' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists sessions;")


def drop_table_theaters(cursor):
    """
    Drops the 'theaters' table from the database if it exists.

    This function executes a SQL 'DROP TABLE IF EXISTS' statement to remove the 'theaters' table, preventing errors if the table does not already exist.

    Args:
        cursor (mysql.connector.cursor.MySQLCursor): A database cursor object used to execute SQL queries.
    """
    cursor.execute("drop table if exists theaters;")