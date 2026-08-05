from Handlers.GreetingHandler import GreetingHandler
from Handlers.IdentityHandler import IdentityHandler
from Handlers.MemoryHandler import MemoryHandler
from Handlers.QuestionHandler import QuestionHandler


class HandlerManager:


    def __init__(self):

        self.handlers = []


        self.register(
            GreetingHandler()
        )

        self.register(
            IdentityHandler()
        )

        self.register(
            MemoryHandler()
        )

        self.register(
            QuestionHandler()
        )



    # =====================================
    # Processamento
    # =====================================

    def process(self, context, manager):

        for handler in self.handlers:


            resposta = handler.process(

                context,

                manager

            )


            if resposta is not None:


                context.set(

                    "current_handler",

                    handler.__class__.__name__

                )


                return resposta


        return None



    # =====================================
    # Registro
    # =====================================

    def register(self, handler):

        self.handlers.append(
            handler
        )



    # =====================================
    # Consulta
    # =====================================

    def get_handlers(self):

        return self.handlers