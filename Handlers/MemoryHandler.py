from Handlers.BaseHandler import BaseHandler


class MemoryHandler(BaseHandler):

    def process(self, message, manager, original_message):

        memory = manager.get("memory")


        # Aprender o nome do usuário
        if message.startswith("meu nome é"):

            nome = original_message[len("meu nome é"):].strip()

            memory.save("user_name", nome)

            return f"Entendido. Vou lembrar que seu nome é {nome}."


        # Consultar o nome do usuário
        if (
    message == "meu nome"
    or "qual meu nome" in message
    or "qual o meu nome" in message
):

            nome = memory.load("user_name")

            if nome:

                return f"Seu nome é {nome}."

            else:

                return "Ainda não sei seu nome."


        return None