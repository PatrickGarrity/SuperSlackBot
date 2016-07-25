class SlackMessage:
    """Represents a Slack message received by Iris."""
    def __init__(self, user, channel, content):
        self.user = user
        self.channel = channel
        self.content = content
