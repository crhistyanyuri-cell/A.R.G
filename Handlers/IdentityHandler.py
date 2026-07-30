class IdentityHandler:

    def process(self, message, manager, original_message):

        config = manager.get("config")

        if "seu nome" in message:
            return f"Meu nome é {config.get('name')}."

        if "sua versão" in message:
            return f"Minha versão atual é {config.get('version')}."

        return None