class ConfigVpc:

    def __init__(self, config) -> None:
        self.config = config

    @property
    def name(self):
        return self.config['name']
