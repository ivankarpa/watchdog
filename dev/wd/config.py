import configparser


class Config:
    def __init__(self, file_name):
        try:
            self.config = configparser.ConfigParser({'port': '9090'})
            if not len(self.config.read(file_name)):
                print("Config file not found")
                raise FileNotFoundError()
        except configparser.MissingSectionHeaderError:
                print("Missing section in config file")
                raise ValueError()

    def get_option(self, section, option):
        try:
            return True, str(self.config.get(section, option))
        except (configparser.NoOptionError, KeyError):
            return False, ""

