from Handlers.BaseHandler import BaseHandler

from Intent.IntentTypes import IntentTypes


class MemoryHandler(BaseHandler):


    def process(self, context, manager):

        intent = context.get("intent")

        original_message = context.get(
            "original_message"
        )

        memory_manager = manager.get(
            "memory_manager"
        )


        # Aprender nome do usuário
        if intent == IntentTypes.REMEMBER_USER_NAME:

            nome = self.extract_name(
                original_message
            )


            if not nome:

                return (
                    "Não consegui identificar "
                    "seu nome."
                )


            nome_antigo = (
                memory_manager.get_user_name()
            )


            memory_manager.set_user_name(
                nome
            )


            if (
                nome_antigo
                and
                nome_antigo != nome
            ):

                return (
                    f"Atualizei seu nome. "
                    f"Agora vou lembrar que "
                    f"você é {nome}."
                )


            return (
                f"Entendido. "
                f"Vou lembrar que "
                f"seu nome é {nome}."
            )


        # Informar nome
        if intent == IntentTypes.ASK_USER_NAME:

            nome = (
                memory_manager.get_user_name()
            )


            if nome:

                return (
                    f"Seu nome é {nome}."
                )


            return (
                "Ainda não sei seu nome."
            )


        return None


    def extract_name(self, message):

        prefixes = [

            "meu nome é",

            "meu nome:",

            "me chamo"

        ]


        texto = message.lower()


        for prefix in prefixes:

            if texto.startswith(prefix):

                return (
                    message[
                        len(prefix):
                    ].strip()
                )


        return None