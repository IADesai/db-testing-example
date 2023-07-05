from unittest.mock import MagicMock

from database import get_all_messages, get_all_messages_no_with


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