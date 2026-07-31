from Handlers.BaseHandler import BaseHandler
from Intent.IntentTypes import IntentTypes


class MemoryHandler(BaseHandler):

    def process(self, context, manager):

        intent = context.get("intent")
        original_message = context.get("original_message")

        memory = manager.get("memory")


        # Aprender o nome do usuário
        if intent == IntentTypes.REMEMBER_USER_NAME:

            nome = original_message[10:].strip()

            memory.save("user_name", nome)

            return f"Entendido. Vou lembrar que seu nome é {nome}."


        # Informar o nome do usuário
        if intent == IntentTypes.ASK_USER_NAME:

            nome = memory.load("user_name")

            if nome:

                return f"Seu nome é {nome}."

            return "Ainda não sei seu nome."


        return None