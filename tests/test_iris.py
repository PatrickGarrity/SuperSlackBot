import unittest
import iris


class ExampleHandler(iris.IrisHandler):
    """Example command handler used to track whether a command has executed."""
    has_executed = False

    def handle_command(self, command):
        self.has_executed = True


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
        event = {"type": "message", "text": "!", "user": "", "channel": ""}
        self.assertTrue(self.bot._is_command(event))
        unrecognized_event = {"type": "message", "text": "not_a_command", "user": "", "channel": ""}
        self.assertFalse(self.bot._is_command(unrecognized_event))

    def test_is_command_malformed(self):
        """_is_command should return false if the event is missing any fields"""
        event_no_channel = {"type": "message", "text": "!", "user": ""}
        event_no_user = {"type": "message", "text": "!", "channel": ""}
        event_no_text = {"type": "message", "channel": "", "user": ""}
        event_no_type = {"text": "!", "user": "", "channel": ""}
        self.assertFalse(self.bot._is_command(event_no_channel))
        self.assertFalse(self.bot._is_command(event_no_user))
        self.assertFalse(self.bot._is_command(event_no_text))
        self.assertFalse(self.bot._is_command(event_no_type))

    def test_conversion_to_command(self):
        """_to_command should convert a well-formed event to an IrisCommand object"""
        event = {"type": "message", "text": "!command_name command_content", "user": "u", "channel": "c"}
        command = self.bot._to_command(event)
        self.assertEqual(command.name, "command_name")
        self.assertEqual(command.content, "command_content")
        self.assertEqual(command.user, "u")
        self.assertEqual(command.channel, "c")

    def test_handle_command_not_recognized(self):
        """handle_command should fail to handle an unrecognized command"""
        command = iris.IrisCommand("name", "user", "channel", "content")
        self.assertFalse(self.bot.handle_command(command))

    def test_handle_command(self):
        """handle_command should handle a registered command"""
        command = iris.IrisCommand("command_name", "user", "channel", "content")
        test_handler = ExampleHandler()
        test_bot = iris.Iris("", {"command_name": test_handler})
        self.assertFalse(test_handler.has_executed)
        test_bot.handle_command(command)
        self.assertTrue(test_handler.has_executed)

if __name__ == '__main__':
    unittest.main()
