import logging


logging.basicConfig(format='%(name)s - %(threadName)s - %(message)s', force=True)
formatter = logging.Formatter('%(name)s - %(threadName)s - %(message)s')

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)