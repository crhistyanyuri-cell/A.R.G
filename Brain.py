import string

from Handlers.GreetingHandler import GreetingHandler
from Handlers.IdentityHandler import IdentityHandler
from Handlers.MemoryHandler import MemoryHandler
from Handlers.QuestionHandler import QuestionHandler


class Brain:

    def __init__(self):

        self.last_thought = None

        self.handlers = [
            GreetingHandler(),
            IdentityHandler(),
            MemoryHandler(),
            QuestionHandler()
        ]


    def think(self, message, manager):

        context = manager.get("context")
        config = manager.get("config")

        original_message = message.strip()

        processed_message = (
            original_message
            .lower()
            .translate(
                str.maketrans("", "", string.punctuation)
            )
            .strip()
        )

        # Atualiza o contexto
        context.set("original_message", original_message)
        context.set("message", processed_message)

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

                # Debug
                if config.get("debug"):
                    self._debug_context(context)

                return resposta

        # Caso nenhum handler responda
        if config.get("debug"):
            self._debug_context(context)

        return "Ainda estou aprendendo."


    def _debug_context(self, context):

        print("\n========== DEBUG ==========")

        for chave, valor in context.context.items():

            print(f"{chave}: {valor}")

        print("===========================\n")