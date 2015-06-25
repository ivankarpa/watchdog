import datetime

LOG_ERROR = 1
LOG_WARNING = 2
LOG_MESSAGE = 3
LOG_DEBUG = 4


class Logger:
    log_file = None

    def initialize(self, file_name):
        try:
            self.log_file = open(file_name, 'w')
            return True
        except:
            return False

    def log_message(self, severity, message):
        if self.log_file and len(message) > 0:
            msg = "{0} {1} {2}\n".format(self.get_time(), severity, message)
            self.log_file.write(msg)
            self.log_file.flush()
        else:
            return False

    def finalize(self):
        if self.log_file:
            self.log_file.close()
            self.log_file = None

    def get_time(self):
        return datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')

    def error(self, message):
        self.log_message(LOG_ERROR, message)

    def warning(self, message):
        self.log_message(LOG_WARNING, message)

    def message(self, message):
        self.log_message(LOG_MESSAGE, message)

    def debug(self, message):
        self.log_message(LOG_DEBUG, message)
