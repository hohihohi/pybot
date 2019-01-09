import os
from slackbot.bot import default_reply

from .hello import hello  # NOQA
from .helper import log_message  # NOQA


DEFAULT_REPLY = f"Sorry, I didn't understand your operation"


@default_reply
@log_message
def deafult_reply_handler(message):
    reply = os.environ.get("DEFAULT_REPLY", DEFAULT_REPLY)
    message.reply(reply)
