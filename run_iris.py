from iris.iris import Iris
from iris.handlers.iris_help import IrisHelpHandler
from iris.analyzers.karma import KarmaAnalyzer

handlers = {
    "help": IrisHelpHandler()
}

analyzers = [KarmaAnalyzer()]

slack_token = ""

iris = Iris(slack_token, handlers, analyzers)
iris.run()
