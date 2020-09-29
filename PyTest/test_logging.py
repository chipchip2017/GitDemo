import logging
import pytest

def test_Logging():
    logger = logging.getLogger(__name__)


    fileHander = logging.FileHandler("testlog.log")
    format = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s: %(message)s")
    fileHander.setFormatter(format)

    logger.addHandler(fileHander)

    logger.setLevel(logging.CRITICAL)
    logger.debug("Statement is debug")
    logger.info("Inform Statement")
    logger.warning("Warning")
    logger.error("Error")
    logger.critical("Critical issue")