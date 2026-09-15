import sqlite3
from models import Movie, MovieCreate


def create_connection():
    """Creates a connection to the SQLite database."""
    connection = sqlite3.connect("movies.db")
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    """Creates the movies table in the database if it doesn't exist."""
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()


create_table()


def create_movie(movie: MovieCreate) -> int:
    """
    Adds a new movie to the database.

    Args:
        movie (MovieCreate): A pydantic model containing the title and director of the movie to be created.

    Returns:
        int: The ID of the newly created movie in the database.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies (title, director) VALUES (?, ?)", (movie.title, movie.director))
    connection.commit()
    movie_id = cursor.lastrowid
    connection.close()
    return movie_id


def read_movies():
    """
    Retrieves all movies from the database.

    Returns:
        list: A list of Movie models representing all movies in the database.
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchal