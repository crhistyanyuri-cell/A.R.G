from Intent.IntentTypes import IntentTypes


class IntentDetector:

    # ==========================
    # Frases diretas
    # ==========================

    GREETINGS = {
        "oi",
        "olá",
        "ola",
        "bom dia",
        "boa tarde",
        "boa noite"
    }


    AI_NAME = {
        "seu nome",
        "qual seu nome",
        "qual o seu nome",
        "como você se chama",
        "como voce se chama",
        "quem é você",
        "quem e voce"
    }


    AI_VERSION = {
        "sua versão",
        "sua versao",
        "qual sua versão",
        "qual sua versao"
    }


    AI_LANGUAGE = {
        "seu idioma",
        "qual seu idioma"
    }


    USER_NAME = {
        "meu nome",
        "qual meu nome",
        "qual o meu nome"
    }



    # ==========================
    # Padrões
    # ==========================

    PATTERNS = {

        "meu nome é": IntentTypes.REMEMBER_USER_NAME,

        # Futuramente:
        # "minha idade é": IntentTypes.REMEMBER_USER_AGE,
        # "eu moro em": IntentTypes.REMEMBER_USER_CITY,

    }



    def detect(self, message, context):


        # ==========================
        # Cumprimentos
        # ==========================

        if message in self.GREETINGS:

            return IntentTypes.GREETING



        # ==========================
        # Nome da IA
        # ==========================

        if message in self.AI_NAME:

            return IntentTypes.ASK_AI_NAME



        # ==========================
        # Versão
        # ==========================

        if message in self.AI_VERSION:

            return IntentTypes.ASK_AI_VERSION



        # ==========================
        # Idioma
        # ==========================

        if message in self.AI_LANGUAGE:

            return IntentTypes.ASK_AI_LANGUAGE



        # ==========================
        # Nome do usuário
        # ==========================

        if message in self.USER_NAME:

            return IntentTypes.ASK_USER_NAME



        # ==========================
        # Detecta padrões
        # ==========================

        for pattern, intent in self.PATTERNS.items():

            if message.startswith(pattern):

                return intent



        # ==========================
        # Contexto
        # ==========================

        if message in {

            "e o meu",
            "e o meu nome"

        }:

            if context.get("last_topic") == "identity":

                return IntentTypes.ASK_USER_NAME



        # ==========================
        # Perguntas gerais
        # ==========================

        if message.startswith(
            (
                "o que",
                "quem",
                "como",
                "onde",
                "quando",
                "por que",
                "porque"
            )
        ):

            return IntentTypes.QUESTION



        # ==========================
        # Desconhecido
        # ==========================

        return IntentTypes.UNKNOWN