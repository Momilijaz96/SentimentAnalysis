import sys

sys.path.append("..")  # for parent folder visibility


from config.config import REDIS_URL, logger
from storage.utils import  insert_doc
from celery import Celery
from typing import List
from datetime import datetime
logger.info("REDIS URL: " + REDIS_URL)
app = Celery("worker", broker=REDIS_URL, backend=REDIS_URL)


@app.task
def store_tweet(texts:List,predictions:List):
    logger.debug("Storage worker received the task : ", texts)
    status = []
    for text, p in zip(texts, predictions):
        doc = {
            "tweet": text,
            "prediction": p,
            "created_at": datetime.now().isoformat(),
        }
        s = str(insert_doc(doc))
        status.append(s)
    logger.debug("Storage worker completed the task : ", texts)
    return status 