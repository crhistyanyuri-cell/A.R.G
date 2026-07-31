from Intent.IntentTypes import IntentTypes


class IntentDetector:

    def detect(self, message):

        # Cumprimentos
        if message in [
            "oi",
            "olá",
            "ola",
            "bom dia",
            "boa tarde",
            "boa noite"
        ]:
            return IntentTypes.GREETING


        # Nome da A.R.G.
        if message in [
            "seu nome",
            "qual seu nome",
            "qual o seu nome",
            "como você se chama",
            "como voce se chama",
            "quem é você",
            "quem e voce"
        ]:
            return IntentTypes.ASK_AI_NAME


        # Versão
        if message in [
            "sua versão",
            "sua versao",
            "qual sua versão",
            "qual sua versao"
        ]:
            return IntentTypes.ASK_AI_VERSION


        # Idioma
        if message in [
            "seu idioma",
            "qual seu idioma"
        ]:
            return IntentTypes.ASK_AI_LANGUAGE


        # Aprender nome do usuário
        if message.startswith("meu nome é"):
            return IntentTypes.REMEMBER_USER_NAME


        # Perguntar nome do usuário
        if message in [
            "meu nome",
            "qual meu nome",
            "qual o meu nome",
            "e o meu nome",
            "e o meu"
        ]:
            return IntentTypes.ASK_USER_NAME


        return IntentTypes.UNKNOWN