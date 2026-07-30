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

        # Mensagem original (preserva maiúsculas)
        original_message = message.strip()

        # Mensagem normalizada para interpretação
        processed_message = (
            original_message
            .lower()
            .translate(
                str.maketrans("", "", string.punctuation)
            )
            .strip()
        )

        # Passa por todos os handlers
        for handler in self.handlers:

            resposta = handler.process(
                processed_message,
                manager,
                original_message
            )

            if resposta is not None:

                self.last_thought = resposta

                return resposta

        return "Ainda estou aprendendo."