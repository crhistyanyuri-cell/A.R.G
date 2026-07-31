class Logger:

    def __init__(self, config):

        self.config = config


    def is_debug(self):

        return self.config.get("debug")


    def debug(self, message):

        if self.is_debug():

            print(f"[DEBUG] {message}")


    def info(self, message):

        print(f"[INFO] {message}")


    def warning(self, message):

        print(f"[WARNING] {message}")


    def error(self, message):

        print(f"[ERROR] {message}")
