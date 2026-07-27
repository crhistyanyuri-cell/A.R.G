class InputManager:

    def __init__(self):

        self.last_input = ""

    def get_input(self):

        self.last_input = input("> ")

        return self.last_input
