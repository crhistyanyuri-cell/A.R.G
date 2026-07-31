from Handlers.BaseHandler import BaseHandler


class QuestionHandler(BaseHandler):

    def process(self, context, manager):

        intent = context.get("intent")

        # Futuramente responderá perguntas gerais

        return None