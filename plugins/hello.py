from slackbot.bot import respond_to

from .helper import log_message


@respond_to("^hello(.*)$")
@log_message
def hello(message, text):
    message.send(f"hello {text}")
