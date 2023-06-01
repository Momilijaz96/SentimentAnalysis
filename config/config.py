# Inside config.py, we'll add the code to define key directory locations

from pathlib import Path
import logging, logging.handlers
from rich.logging import RichHandler
import sys
import os


def get_env(env_name: str) -> str:
    try:
        return os.environ[env_name]
    except KeyError:
        # hacky way to read env vars from /env file for debugging  purpose
        env_dir = Path(__file__).resolve().parent.parent.absolute() / "env"
        for env_file in env_dir.glob("*.env"):
            if env_file.exists():
                with open(env_file, "r") as f:
                    for line in f.readlines():
                        if line.startswith(env_name):
                            return line.split("=")[-1].strip()
            else:
                raise Exception(f"Environment variable {env_name} not set.")
            # raise Exception(f"Environment variable {env_name} not set.")


# Directories
BASE_DIR = Path(__file__).resolve().parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR / "config")
MODEL_SAVE_PATH = Path(BASE_DIR / "saved_model" / "distil_bert_emotion_ckpt")

# Declare id2label and label2id mappings
label2id = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

id2label = {v: k for k, v in label2id.items()}

# MONGO DB connection string
mongodb_password = get_env("MONGODB_PASSWORD")
mongodb_username = get_env("MONGODB_USERNAME")
CLUSTER_NAME = get_env("CLUSTER_NAME")
DB_NAME = get_env("DB_NAME")
COLLECTION_NAME = get_env("COLLECTION_NAME")

DB_CONNECTION_STRING = f"mongodb+srv://{mongodb_username}:{mongodb_password}@{CLUSTER_NAME}.uaunqgg.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

# Redis connection for API2Model message queue
REDIS_HOST = get_env("REDIS_HOST")
REDIS_PORT = get_env("REDIS_PORT")
REDIS_DB = get_env("REDIS_DB")
REDIS_QUEUE_NAME = get_env("REDIS_QUEUE_NAME")
REDIS_USERNAME = get_env("REDIS_USERNAME")
REDIS_PASSWORD = get_env("REDIS_PASSWORD")
REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"


# Set logging configurations
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Get root logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create handlers
console_handler = RichHandler(markup=True)
console_handler.setLevel(logging.DEBUG)
info_handler = logging.handlers.RotatingFileHandler(
    filename=Path(LOGS_DIR, "info.log"),
    maxBytes=10485760,  # 1 MB
    backupCount=10,
)
info_handler.setLevel(logging.INFO)
error_handler = logging.handlers.RotatingFileHandler(
    filename=Path(LOGS_DIR, "error.log"),
    maxBytes=10485760,  # 1 MB
    backupCount=10,
)
error_handler.setLevel(logging.ERROR)

# Create formatters
minimal_formatter = logging.Formatter(fmt="%(message)s")
detailed_formatter = logging.Formatter(
    fmt="%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
)

# Hook it all up
console_handler.setFormatter(fmt=minimal_formatter)
info_handler.setFormatter(fmt=detailed_formatter)
error_handler.setFormatter(fmt=detailed_formatter)
logger.addHandler(hdlr=console_handler)
logger.addHandler(hdlr=info_handler)
logger.addHandler(hdlr=error_handler)
