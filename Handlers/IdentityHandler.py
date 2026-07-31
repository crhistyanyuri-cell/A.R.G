from Handlers.BaseHandler import BaseHandler


class IdentityHandler(BaseHandler):

    def process(self, context, manager):

        message = context.get("message")

        config = manager.get("config")


        if "seu nome" in message:

            return f"Meu nome é {config.get('name')}."


        if "sua versão" in message:

            return f"Minha versão atual é {config.get('version')}."


        if "seu idioma" in message:

            return f"Meu idioma principal é {config.get('language')}."


        return None