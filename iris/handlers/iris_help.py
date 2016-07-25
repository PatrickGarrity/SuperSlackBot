from iris import IrisHandler


class IrisHelpHandler(IrisHandler):
    """Handler that prints usage and other help for the Iris bot."""

    help_text = """
Iris Help
---------
You can interact with the Iris bot by sending commands using the '!' character.
For example, you displayed this help by posting '!help'.
    """

    def handle_command(self, sc, command):
        """Send the help message to the Slack channel where the request was received."""
        sc.rtm_send_message(command.channel, self.help_text)
