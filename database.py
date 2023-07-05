"""This module contains functions used to interact with the database."""

from psycopg2 import connect
from psycopg2.extensions import connection

def get_connection(config: dict) -> connection:
    """Return a database connection."""
    conn = connect(
        dbname=config["DB_NAME"],
        host=config["DB_HOST"],
        port=config["DB_PORT"]
    )
    return conn


def get_all_messages(conn: connection) -> list[str]:
    """Return a list of messages from the database."""
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM message;")
        return cur.fetchall()


def insert_message(conn: connection, text: str) -> tuple[int, str]:
    """Insert a single message into the database and return the message data."""

    if not isinstance(text, str):
        raise TypeError("Message text must be a string.")

    with conn.cursor() as cur:
        cur.execute("""
                    INSERT INTO message (message_text)
                    VALUES (%s)
                    RETURNING *;
                    """, [text])
        conn.commit()
        return cur.fetchone()
