import inspect
import logging

class BaseClass:
    def test_LoggingDemo(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        fileHander = logging.FileHandler("testlog1.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s: %(message)s")
        fileHander.setFormatter(format)

        logger.addHandler(fileHander)

        logger.setLevel(logging.DEBUG)
        return logger