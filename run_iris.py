from iris.iris import Iris
from iris.handlers.iris_help import IrisHelpHandler

handlers = {
    "help": IrisHelpHandler()
}

slack_token = "xoxb-44716617858-BVBafgRqyoLJm1GDnmEm5V6M"

iris = Iris(slack_token, handlers)
iris.run()
