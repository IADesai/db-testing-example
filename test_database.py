import pytest

from unittest.mock import MagicMock

from database import get_all_messages, get_all_messages_no_with, insert_message


def test_get_all_messages_returns_list():

    fake_connection = MagicMock()

    fake_connection.cursor().__enter__().fetchall.return_value = []

    result = get_all_messages(fake_connection)

    assert isinstance(result, list)


def test_get_all_messages_no_with_returns_list():
    """If my function gets specific things, does it behave in expected ways"""

    fake_connection = MagicMock()

    fake_execute = fake_connection.cursor().execute
    fake_fetch = fake_connection.cursor().fetchall
    fake_fetch.return_value = []

    result = get_all_messages_no_with(fake_connection)

    assert isinstance(result, list)
    assert fake_fetch.call_count == 1
    assert fake_execute.call_count == 1
    assert fake_execute.call_args[0] == ("SELECT * FROM message;",)


def test_insert():
    fake_connection = MagicMock()

    fake_execute = fake_connection.cursor().__enter__().execute
    fake_fetch = fake_connection.cursor().__enter__().fetchone
    fake_fetch.return_value = ()
    arg = "Argument"
    result = insert_message(fake_connection, arg)

    assert isinstance(result, tuple)
    assert fake_fetch.call_count == 1
    assert fake_execute.call_count == 1
    assert fake_execute.call_args[0] == ("""
                    INSERT INTO message (message_text)
                    VALUES (%s)
                    RETURNING *;
                    """, [arg])


# def test_insert_raise_Error():
#     fake_connection = MagicMock()

#     arg = []
#     result = insert_message(fake_connection, arg)

#     with pytest.raises(TypeError):
#         Message text must be a string
