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

        learning = manager.get(
            "learning"
        )



        # ==========================
        # Aprender nome do usuário
        # ==========================

        if intent == IntentTypes.REMEMBER_USER_NAME:

            return self._remember_user_name(
                original_message,
                memory_manager,
                learning
            )



        # ==========================
        # Informar nome
        # ==========================

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



        # ==========================
        # Aprender preferência
        # ==========================

        if intent == IntentTypes.REMEMBER_PREFERENCE:

            return self._remember_preference(
                original_message,
                learning
            )



        # ==========================
        # Aprender fato
        # ==========================

        if intent == IntentTypes.REMEMBER_FACT:

            return self._remember_fact(
                original_message,
                learning
            )



        return None



    # ==========================
    # Métodos privados
    # ==========================


    def _remember_user_name(
        self,
        message,
        memory_manager,
        learning
    ):


        nome = self.extract_name(
            message
        )


        if not nome:

            return (
                "Não consegui identificar "
                "seu nome."
            )



        nome_antigo = (
            memory_manager.get_user_name()
        )



        if learning:

            learning.remember_name(
                nome
            )

        else:

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



    # ==========================
    # Preferências
    # ==========================

    def _remember_preference(
        self,
        message,
        learning
    ):


        if not learning:

            return (
                "O módulo de aprendizado "
                "não está disponível."
            )


        texto = message.lower()



        partes = texto.split(
            "é"
        )


        if len(partes) < 2:

            return (
                "Não consegui identificar "
                "essa preferência."
            )



        chave = partes[0]


        chave = chave.replace(
            "minha",
            ""
        )


        chave = chave.replace(
            "favorita",
            ""
        )


        chave = chave.strip()



        valor = partes[1].strip()



        learning.learn_preference(
            chave,
            valor
        )



        return (

            f"Entendido. "

            f"Vou lembrar que sua "

            f"{chave} favorita é {valor}."

        )



    # ==========================
    # Fatos
    # ==========================

    def _remember_fact(
        self,
        message,
        learning
    ):


        if not learning:

            return (
                "O módulo de aprendizado "
                "não está disponível."
            )



        fato = message.replace(
            "lembre que",
            ""
        ).strip()



        if not fato:

            return (
                "Não consegui identificar "
                "o fato."
            )



        learning.learn_fact(
            fato
        )



        return (

            "Entendido. "

            "Vou guardar essa informação."

        )



    def extract_name(self, message):


        prefixes = {

            "meu nome é",

            "meu nome:",

            "me chamo"

        }



        texto = message.lower()



        for prefix in prefixes:


            if texto.startswith(prefix):

                return (

                    message[
                        len(prefix):
                    ].strip()

                )



        return None