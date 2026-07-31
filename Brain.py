import string

from Intent.IntentDetector import IntentDetector

from Handlers.GreetingHandler import GreetingHandler
from Handlers.IdentityHandler import IdentityHandler
from Handlers.MemoryHandler import MemoryHandler
from Handlers.QuestionHandler import QuestionHandler


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

        # Detecta a intenção
        intent = self.intent_detector.detect(processed_message)

        # Atualiza o contexto
        context.set("original_message", original_message)
        context.set("message", processed_message)
        context.set("intent", intent)

        # Percorre todos os handlers
        for handler in self.handlers:

            resposta = handler.process(
                context,
                manager
            )

            if resposta is not None:

                self.last_thought = resposta

                context.set("last_response", resposta)
                context.set(
                    "current_handler",
                    handler.__class__.__name__
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

        self._debug_context(
            context,
            logger
        )

        return self.last_thought


    def _debug_context(self, context, logger):

        logger.debug("")
        logger.debug("========== DEBUG ==========")

        for chave, valor in context.context.items():

            logger.debug(f"{chave}: {valor}")

        logger.debug("===========================")
        logger.debug("")