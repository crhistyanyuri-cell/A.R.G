from Handlers.BaseHandler import BaseHandler
from Intent.IntentTypes import IntentTypes


class GreetingHandler(BaseHandler):

    def process(self, context, manager):

        intent = context.get("intent")

        if intent == IntentTypes.GREETING:

            return "Olá!"

        return None