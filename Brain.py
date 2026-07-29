class Brain:

    def think(self, message):

        message = message.lower().strip()

        resposta = self.handle_greetings(message)

        if resposta:
            return resposta

        return "Ainda estou aprendendo."

    def handle_greetings(self, message):

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