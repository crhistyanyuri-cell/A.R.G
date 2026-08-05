import string

from Intent.IntentDetector import IntentDetector


class Brain:

    def __init__(self):

        self.last_thought = None

        self.intent_detector = IntentDetector()


    def think(self, message, manager):

        logger = manager.get("logger")
        context = manager.get("context")

        original_message = message.strip()

        processed_message = self._normalize(
            original_message
        )

        intent = self.intent_detector.detect(

            processed_message,

            context

        )

        context.update_intent(intent)

        context.set(
            "original_message",
            original_message
        )

        context.set(
            "message",
            processed_message
        )

        handler_manager = manager.get(
            "handler_manager"
        )

        resposta = handler_manager.process(

            context,

            manager

        )

        if resposta is None:

            resposta = "Ainda estou aprendendo."

            context.set(
                "current_handler",
                "Nenhum"
            )

        self.last_thought = resposta

        context.set(
            "last_response",
            resposta
        )

        context.add_history(

            original_message,

            resposta,

            intent

        )

        self._debug_context(

            context,

            logger

        )

        return resposta


    def _normalize(self, message):

        return (

            message

            .lower()

            .translate(

                str.maketrans(

                    "",

                    "",

                    string.punctuation

                )

            )

            .strip()

        )


    def _debug_context(self, context, logger):

        logger.debug("")
        logger.debug("========== DEBUG ==========")

        logger.debug(
            f"Mensagem: {context.get('message')}"
        )

        logger.debug(
            f"Intenção: {context.get('intent')}"
        )

        logger.debug(
            f"Handler: {context.get('current_handler')}"
        )

        logger.debug(
            f"Resposta: {context.get('last_response')}"
        )

        logger.debug("")
        logger.debug("Histórico:")

        for item in context.get_history():

            logger.debug(item)

        logger.debug("===========================")
        logger.debug("")