# Inside config.py, we'll add the code to define key directory locations

from pathlib import Path
import logging
import sys

# Directories
BASE_DIR = Path(__file__).resolve().parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR / "config")
MODEL_SAVE_PATH = Path(BASE_DIR / "saved_model" / "distil_bert_emotion_ckpt")

# Declare id2label and label2id mappings
label2id = {"sadness": 0, "joy": 1, "love": 2, "anger": 3, "fear": 4, "surprise": 5}

id2label = {v: k for k, v in label2id.items()}

# DB connection string
DB_CONNECTION_STRING = "mongodb+srv://MomalIjaz:<RKvCezMGr2Fnpyxt>@tweetssentiment.uaunqgg.mongodb.net/test"
DB_NAME = "TweetsSentiment"

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
