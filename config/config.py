# Inside config.py, we'll add the code to define key directory locations

from pathlib import Path
import logging
import sys
import os
from dynaconf import Dynaconf


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
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "root": {
        "handlers": ["console", "info", "error"],
        "level": logging.INFO,
        "propagate": True,
    },
}
# logging.config.dictConfig(logging_config)
logger = logging.getLogger()
