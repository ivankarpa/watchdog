import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser({'port': '9090'})
        self.config.read('watchdog.cfg')

    def get_option(self, section, option):
        try:
            return True, str(self.config.get(section, option))
        except (configparser.NoOptionError, KeyError):
            return False, ""
