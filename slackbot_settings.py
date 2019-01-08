from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(verbose=True, dotenv_path=env_path)

API_TOKEN = os.getenv("API_TOKEN") or os.environ["API_TOKEN"]
DEFAULT_REPLY = "Hello"
PLUGINS = ['plugins'] # directory name of plugin
