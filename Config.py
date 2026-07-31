class Config:

    def __init__(self):

        self.config = {

        "name": "A.R.G.",
        "version": "0.1.1",
        "language": "pt-BR",
        "debug": True

}

    def get(self, key):

        return self.config.get(key)

    def set(self, key, value):

        self.config[key] = value
        self.config["debug"] = True