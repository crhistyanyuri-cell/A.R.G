class ContextManager:

    def __init__(self):

        self.context = {

        "message": None,
        "original_message": None,
        "last_response": None,
        "current_handler": None

}

    def set(self, key, value):

        self.context[key] = value

    def get(self, key):

        return self.context.get(key)

    def clear(self):

        self.context = {

    "message": None,
    "original_message": None,
    "last_response": None,
    "current_handler": None

}