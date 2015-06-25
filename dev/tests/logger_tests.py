import unittest
import sys
import datetime

sys.path.append('../shared/')
import logger


class ConfigParserTest(unittest.TestCase):
    VALID_MESSAGE = 'Test message' + datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
    EMPTY_MESSAGE = ''
    VALID_FILENAME = "test.log"
    INVALID_FILENAME = 'te\0st.log'
    EMPTY_FILENAME = ''
    ERROR_SEVERITY = '1'
    WARNING_SEVERITY = '2'
    MESSAGE_SEVERITY = '3'
    DEBUG_SEVERITY = '4'

    def read_last_record(self):
        file = open(self.VALID_FILENAME, 'r')
        all_records = file.readlines()
        file.close()
        return all_records[-1]

    def setUp(self):
        self.log = logger.Logger()

    def test_log_with_valid_data(self):
        self.log.initialize(self.VALID_FILENAME)
        self.log.log_message(self.MESSAGE_SEVERITY, self.VALID_MESSAGE)
        self.log.finalize()
        self.assertIn(self.VALID_MESSAGE, self.read_last_record())

    def test_log_with_invalid_filename(self):
        self.assertFalse(self.log.initialize(self.INVALID_FILENAME))
        self.assertFalse(self.log.initialize(self.EMPTY_FILENAME))

    def test_log_empty_message(self):
        self.log.initialize(self.VALID_FILENAME)
        self.assertFalse(self.log.log_message(self.MESSAGE_SEVERITY, self.EMPTY_MESSAGE))
        self.log.finalize()

    def test_log_error(self):
        self.log.initialize(self.VALID_FILENAME)
        self.log.error(self.VALID_MESSAGE)
        self.log.finalize()
        self.assertIn(self.ERROR_SEVERITY+' '+self.VALID_MESSAGE, self.read_last_record())

    def test_log_warning(self):
        self.log.initialize(self.VALID_FILENAME)
        self.log.warning(self.VALID_MESSAGE)
        self.log.finalize()
        self.assertIn(self.WARNING_SEVERITY+' '+self.VALID_MESSAGE, self.read_last_record())

    def test_log_message(self):
        self.log.initialize(self.VALID_FILENAME)
        self.log.message(self.VALID_MESSAGE)
        self.log.finalize()
        self.assertIn(self.MESSAGE_SEVERITY+' '+self.VALID_MESSAGE, self.read_last_record())

    def test_log_debug(self):
        self.log.initialize(self.VALID_FILENAME)
        self.log.debug(self.VALID_MESSAGE)
        self.log.finalize()
        self.assertIn(self.DEBUG_SEVERITY+' '+self.VALID_MESSAGE, self.read_last_record())


if __name__ == '__main__':
    unittest.main()
