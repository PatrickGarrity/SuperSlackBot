import time

from iris.iriscommand import IrisCommand
from iris.signalhandler import ExitOnSignal
from slackclient import SlackClient


class Iris:
    """The Iris Slack bot engine."""

    def __init__(self, slack_token, command_handlers):
        self.sc = SlackClient(slack_token)
        self.command_handlers = command_handlers
        self._signal_handler = ExitOnSignal()

    def run(self):
        """Run the Iris bot using the configured commands."""
        if self.sc.rtm_connect():
            print("> Successfully connected to Slack! Starting the Iris bot...")
            while True:
                # Check the signal handler to make sure we are breaking if necessary.
                if self._signal_handler.kill_now:
                    print("> Terminating the Iris bot...")
                    break

                # Read events from Slack, then parse that list of events into IrisCommand objects.
                events = self.sc.rtm_read()
                commands = self.convert_commands(self.filter_commands(events))

                # Handle each IrisCommand received from Slack.
                for command in commands:
                    self.handle_command(command)

                # Sleep so that we're polite to Slack. There does not seem to be a blocking
                # approach available at this time so this will have to do.
                time.sleep(0.1)
        else:
            print("Failed to connect to Slack. Please verify you have a valid token.")

    @staticmethod
    def _is_command(event):
        """True if the event is a command, false otherwise. Commands are Slack messages that start with '!',
        the command identifier, and contain all required fields."""
        if 'type' in event and 'text' in event and 'user' in event and 'channel' in event:
            return event['type'] == 'message' and str(event['text']).startswith("!")
        else:
            return False

    @staticmethod
    def _command_name(cmd):
        """Extract the name of a command."""
        # We say that the name is any character up until the first space.
        # When we use this command, we already know that the string starts with an '!', the command identifier.
        # We ignore the command identifier with [:1], and then take a single split by space. The single split
        # will produce an array of size two with the first element being to the left of the space, and the second
        # element being to the right of the space. We'll use this same approach to extract the content as well.
        return str(cmd['text'])[1:].split(" ", 1)[0]

    @staticmethod
    def _command_content(cmd):
        """Extract the content of a command."""
        splits = str(cmd['text']).split(" ", 1)
        if len(splits) > 1:
            return splits[1]
        else:
            return ""

    def _to_command(self, cmd):
        """Builds an IrisCommand from the given Slack event."""
        return IrisCommand(self._command_name(cmd), cmd['user'], cmd['channel'], self._command_content(cmd))

    def filter_commands(self, events):
        """Given some list of events, filter such that only the commands remain."""
        return list(filter(lambda evt: self._is_command(evt), events))

    def convert_commands(self, commands):
        """Given some list of commands, convert them into IrisCommand objects."""
        return list(map(lambda cmd: self._to_command(cmd), commands))

    def handle_command(self, command):
        """Given some command, parse it and act upon it if the command is registered."""
        if command.name in self.command_handlers:
            handler = self.command_handlers[command.name]
            handler.handle_command(self.sc, command)
            return True
        else:
            print("No handler exists for command \'" + command.name + "\'.")
            self.sc.rtm_send_message(command.channel,
                                     "No such command \'" + command.name + "\' exists, please type !help for a list.")
            return False
