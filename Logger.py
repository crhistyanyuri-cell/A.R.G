class Logger:

    def __init__(self):
        pass

    def info(self, message):
        print(f"[INFO] {message}")

    def warning(self, message):
        print(f"[WARNING] {message}")

    def error(self, message):
        print(f"[ERROR] {message}")
