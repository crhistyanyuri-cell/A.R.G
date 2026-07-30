from Handlers.BaseHandler import BaseHandler


class GreetingHandler(BaseHandler):

    def process(self, message, manager, original_message):

        cumprimentos = [
            "oi",
            "olá",
            "ola",
            "bom dia",
            "boa tarde",
            "boa noite"
        ]

        if message in cumprimentos:
            return "Olá!"

        return None