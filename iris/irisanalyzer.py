class IrisAnalyzer:
    def analyze_message(self, sc, message):
        """Default implementation simply prints the message that was received."""
        print("Default implementation received message: " + message.content)
