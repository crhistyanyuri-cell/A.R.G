class CommandProcessor:

    def __init__(self):

        self.last_command = ""

    def process(self, text):

        self.last_command = text

        if text.startswith("/"):
            return "command"

        return {
    "type": "message",
    "content": text
}
