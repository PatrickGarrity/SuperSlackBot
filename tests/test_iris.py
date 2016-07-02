import unittest
from iris import iris


class TestIris(unittest.TestCase):
    bot = iris.Iris("", {})

    def test_command_name(self):
        """_command_name should produce the name of the command"""
        command = {"text": "!command_name"}
        self.assertEqual(self.bot._command_name(command), "command_name")

    def test_command_content_no_content(self):
        """_command_content should produce empty content if there is no content"""
        command = {"text": "!command_name"}
        self.assertEqual(self.bot._command_content(command), "")

    def test_command_content(self):
        """_command_content should produce empty content if there is no content"""
        command = {"text": "!command_name command_content"}
        self.assertEqual(self.bot._command_content(command), "command_content")

    def test_is_command(self):
        """_is_command should return true if the event text starts with a command identifier"""
        event = {"type": "message", "text": "!"}
        self.assertTrue(self.bot._is_command(event))
        unrecognized_event = {"type": "message", "text": "not_a_command"}
        self.assertFalse(self.bot._is_command(unrecognized_event))

if __name__ == '__main__':
    unittest.main()
