import unittest
from unittest.mock import patch, MagicMock
import chat_handler


class TestChatHandler(unittest.TestCase):
    def setUp(self):
        self.message = "Hello, world!"

    def test_store_conversation(self):
        # reset the conversations
        chat_handler.conversations = {}
        chat_handler.store_conversation("user", self.message)
        self.assertEqual(chat_handler.conversations["user"], [self.message])

    def test_get_conversation(self):
        # reset the conversations
        chat_handler.conversations = {}
        # First store a message
        chat_handler.store_conversation("user", self.message)
        # Then get the conversation
        result = chat_handler.get_conversation("user")
        # Assert that the result is the same as the message
        self.assertEqual(result, [self.message])


if __name__ == '__main__':
    unittest.main()
