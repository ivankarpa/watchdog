import configparser



class Config:
    def __init__(self, file_name):
        self.file_name = file_name
        self.config = configparser.ConfigParser({'port': '9090'})
        try:
            self.config.read(self.file_name)
        except configparser.MissingSectionHeaderError:
            pass

    def get_option(self, section, option):
            try:
                return True, str(self.config.get(section, option))
            except (configparser.NoOptionError, KeyError):
                return False, ""
            except (configparser.NoSectionError, KeyError):
                return False, ""

