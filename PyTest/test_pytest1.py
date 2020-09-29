import pytest

from PyTest.BaseClass import BaseClass


class TestExample1(BaseClass):
    def test_Log(self):
        log = self.test_LoggingDemo()
        log.info("Nhi1")
