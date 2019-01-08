import os

import notification
from helper import log_message


DEFAULT_REPLY = f"Default message: {message.body['text']} accepted"

@default_reply
@log_message
def deafult_reply_handler(message):
    reply = os.environ["DEFAULT_REPLY"] or DEFAULT_REPLY
    message.reply(reply)