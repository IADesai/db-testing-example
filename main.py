"""This module is used to connect to the database and carry out basic operations."""

from database import get_connection, get_all_messages, insert_message

if __name__ == "__main__":

    config = {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "testing_example_prod",
    }

    conn = get_connection(config)

    print(insert_message(conn, "green"))
    print(get_all_messages(conn))