class Logger:

    def __init__(self, config):

        self.config = config


    def debug(self, message):

        if self.config.get("debug"):

            print(f"[DEBUG] {message}")


    def info(self, message):

        print(f"[INFO] {message}")


    def warning(self, message):

        print(f"[WARNING] {message}")


    def error(self, message):

        print(f"[ERROR] {message}")
