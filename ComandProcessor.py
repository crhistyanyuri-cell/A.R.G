class CommandProcessor:

    def __init__(self):

        self.last_command = ""

    def process(self, text):

        self.last_command = text

        if text.startswith("/"):

            return {
                "type": "command",
                "content": text[1:].lower()
            }

        return {
            "type": "message",
            "content": text
        }
