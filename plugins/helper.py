from slackbot_settings import ERRORS_TO


def log_message(func):
    def wrapper(message, *args):
        text = f"Received message from <@{message.body['user']}> in <#{message.body['channel']}>: {message.body['text']}"
        print(text)
        message._client.send_message(f"@{ERRORS_TO}", text, as_user=True)
        return func(message, *args)
    return wrapper
