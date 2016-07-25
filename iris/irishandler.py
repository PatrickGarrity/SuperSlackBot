class IrisHandler:
    def handle_command(self, sc, command):
        """Default implementation simply prints the command name."""
        print("Default implementation received command \'" + command.name + "\'.")
