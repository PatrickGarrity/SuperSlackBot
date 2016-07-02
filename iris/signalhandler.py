import signal


class ExitOnSignal:
    """Used to handle signals to gracefully shutdown Iris."""

    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.trigger_shutdown)
        signal.signal(signal.SIGTERM, self.trigger_shutdown)

    def trigger_shutdown(self, signum, frame):
        self.kill_now = True
