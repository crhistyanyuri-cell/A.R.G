class Config:

    def __init__(self):

        self.config = {

            "name": "A.R.G",
            "version": "0.3.0",
            "language": "pt-BR",
            "debug": False

        }

    def get(self, key):

        return self.config.get(key)

    def set(self, key, value):

        self.config[key] = value