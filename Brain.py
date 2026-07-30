class Brain:

    def __init__(self):
        self.last_thought = None


    def think(self, message, manager):

        original_message = message.strip()

        message = message.lower().strip()


        handlers = [
            self.handle_identity,
            self.handle_greetings,
            self.handle_memory,
            self.handle_questions
        ]


        for handler in handlers:

            resposta = handler(
                message,
                manager,
                original_message
            )

            if resposta:

                self.last_thought = resposta

                return resposta


        return "Ainda estou aprendendo."



    def handle_identity(self, message, manager, original_message):

        config = manager.get("config")


        if "seu nome" in message:

            nome = config.get("name")

            return f"Meu nome é {nome}."


        if "sua versão" in message:

            version = config.get("version")

            return f"Minha versão atual é {version}."


        if "seu idioma" in message:

            language = config.get("language")

            return f"Meu idioma principal é {language}."


        return None



    def handle_greetings(self, message, manager, original_message):

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



    def handle_memory(self, message, manager, original_message):

        memory = manager.get("memory")


        if message.startswith("meu nome é"):

            nome = original_message[11:].strip()

            memory.save("user_name", nome)

            return f"Entendido. Vou lembrar que seu nome é {nome}."


        if "qual meu nome" in message:

            nome = memory.load("user_name")


            if nome:

                return f"Seu nome é {nome}."


            else:

                return "Ainda não sei seu nome."


        return None



    def handle_questions(self, message, manager, original_message):

        return None