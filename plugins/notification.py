from helper import log_message

@log_message
def notification(message, text):
    message.send(text)