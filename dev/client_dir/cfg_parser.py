import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser({'host': 'localhost', 'port': '9090'})
        self.config.read('client.cfg')

    def get_host(self):
        return str(self.config.get('connect', 'host'))

    def get_port(self):
        return int(self.config.get('connect', 'port'))



