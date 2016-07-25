from iris.irisanalyzer import IrisAnalyzer


class KarmaAnalyzer(IrisAnalyzer):
    """Karma implementation that looks for messages intended to grant or take karma."""

    def analyze_message(self, sc, message):
        """WIP: Tell the user karma has been granted if there is a match..."""
        print("Analyzing message \'" + message.content + "\' for karma.")
