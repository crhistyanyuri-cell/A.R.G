from Intent.IntentDetector import IntentDetector

from Handlers.GreetingHandler import GreetingHandler
from Handlers.IdentityHandler import IdentityHandler
from Handlers.MemoryHandler import MemoryHandler
from Handlers.QuestionHandler import QuestionHandler

import string


class Brain:

    def __init__(self):

        self.last_thought = None

        # Detector de intenções
        self.intent_detector = IntentDetector()

        # Handlers registrados
        self.handlers = [
            GreetingHandler(),
            IdentityHandler(),
            MemoryHandler(),
            QuestionHandler()
        ]


    def think(self, message, manager):

        logger = manager.get("logger")
        context = manager.get("context")

        # Mensagem original
        original_message = message.strip()

        # Mensagem normalizada
        processed_message = (
            original_message
            .lower()
            .translate(
                str.maketrans("", "", string.punctuation)
            )
            .strip()
        )

        # Detecta a intenção usando o contexto
        intent = self.intent_detector.detect(
            processed_message,
            context
        )

        # Atualiza a intenção
        context.update_intent(intent)

        # Atualiza o contexto
        context.set("original_message", original_message)
        context.set("message", processed_message)

        # Percorre handlers
        for handler in self.handlers:

            resposta = handler.process(
                context,
                manager
            )

            if resposta is not None:

                self.last_thought = resposta

                context.set(
                    "last_response",
                    resposta
                )

                context.set(
                    "current_handler",
                    handler.__class__.__name__
                )

                # Salva no histórico
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


        self.last_thought = "Ainda estou aprendendo."

        context.set(
            "last_response",
            self.last_thought
        )

        context.set(
            "current_handler",
            "Nenhum"
        )

        context.add_history(
            original_message,
            self.last_thought,
            intent
        )

        self._debug_context(
            context,
            logger
        )

        return self.last_thought



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


        for item in context.get("history"):

            logger.debug(item)


        logger.debug("===========================")
        logger.debug("")