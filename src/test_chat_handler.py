import unittest
from unittest.mock import patch, MagicMock
import chat_handler


class TestChatHandler(unittest.TestCase):
    def setUp(self):
        self.message = "Hello there"
        self.response_with_seed = "General Kenobi!"

    def test_handle_chat_message(self):
        result = chat_handler.handle_chat_message(self.message, 400)
        self.assertEqual(result, self.response_with_seed)


if __name__ == '__main__':
    unittest.main()
