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

        original_message = message.strip()

        processed_message = (
            original_message
            .lower()
            .translate(
                str.maketrans("", "", string.punctuation)
            )
            .strip()
        )

        context.set("original_message", original_message)
        context.set("message", processed_message)

        for handler in self.handlers:

            resposta = handler.process(
                processed_message,
                manager,
                original_message
            )

            if resposta is not None:

                self.last_thought = resposta

                context.set("last_response", resposta)

                return resposta

        return "Ainda estou aprendendo."