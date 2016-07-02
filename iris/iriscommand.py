class IrisCommand:
    """Represents a command to the Iris bot."""
    def __init__(self, name, user, channel, content):
        self.name = name
        self.user = user
        self.channel = channel
        self.content = content
