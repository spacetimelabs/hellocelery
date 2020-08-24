import os
from dotenv import load_dotenv

load_dotenv()


BROKER_URL = os.getenv("BROKER_URL")
RESULT_BACKEND_URL = os.getenv("RESULT_BACKEND_URL")
DEFAULT_QUEUE = os.getenv("DEFAULT_QUEUE", "hello")
