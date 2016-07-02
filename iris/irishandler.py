class IrisHandler:
    def handle_command(self, command):
        """Default implementation simply prints the command name."""
        print("Default implementation received command \'" + command.name + "\'.")
