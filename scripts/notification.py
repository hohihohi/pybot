import os
from slackclient import SlackClient
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(".") / ".env"
load_dotenv(verbose=True, dotenv_path=env_path)

slack_token = os.getenv("API_TOKEN") or os.environ["API_TOKEN"]
sc = SlackClient(slack_token)

def post_message(text, channel, upload_file=None):
    if upload_file is not None:
        sc.api_call(
            "files.upload",
            channels=channel,
            initial_comment=text,
            file=upload_file
        )
        return
    sc.api_call(
        "chat.postMessage",
        channel=channel,
        text=text,
        as_user=True 
    )

file_path= Path(".") / "data" / "sample.md"

with open(file_path) as file_content:
    post_message("file upload dayo", "test_shiraishi", file_content) 
post_message("WIP! :tada:", "test_shiraishi")
