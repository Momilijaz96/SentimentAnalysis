# Inside config.py, we'll add the code to define key directory locations

from pathlib import Path
import logging
import sys
import os
from dynaconf import Dynaconf


# Directories
BASE_DIR = Path(__file__).resolve().parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR / "config")
MODEL_SAVE_PATH = Path(BASE_DIR / "saved_model" / "distil_bert_emotion_ckpt")

# Declare id2label and label2id mappings
label2id = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

id2label = {v: k for k, v in label2id.items()}

# MONGO DB connection string
mongodb_password = os.environ["MONGODB_PASSWORD"]
mongodb_username = os.environ["MONGODB_USERNAME"]
CLUSTER_NAME = "tweetstentiment"
DB_NAME = "tweets_db"
COLLECTION_NAME = "tweets_collection"

DB_CONNECTION_STRING = f"mongodb+srv://{mongodb_username}:{mongodb_password}@{CLUSTER_NAME}.uaunqgg.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

# Redis connection for API2Model message queue
REDIS_HOST = "redis-17442.c16.us-east-1-2.ec2.cloud.redislabs.com"
REDIS_PORT = 17442
REDIS_DB = "API2Model-Queue"
REDIS_QUEUE_NAME = "api2model"
REDIS_USERNAME = "default"
REDIS_PASSWORD = "sqm18hv0ZKeYQ7cOyg6Y2SEcPzGHAMhN"
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
