import unittest
from unittest.mock import patch, MagicMock
import chat_handler


class TestChatHandler(unittest.TestCase):
    def setUp(self):
        self.message = "Hello, world!"
        self.response_with_seed = "Hello! How can I assist you today?"

    def test_handle_chat_message(self):
        result = chat_handler.handle_chat_message(self.message)
        self.assertEqual(result, self.response_with_seed)


if __name__ == '__main__':
    unittest.main()
