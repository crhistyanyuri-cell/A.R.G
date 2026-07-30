from typing import Self


class ContextManager:

    def __init__(self):

        self.context = {

            "message": None,
            "original_message": None,
            "last_response": None,
            "user_name": None

        }
    def set(self, key, value):

        self.context[key] = value


def get(self, key):

    return self.context.get(key)    