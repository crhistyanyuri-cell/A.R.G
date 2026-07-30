class BaseHandler:

    def process(self, message, manager, original_message):
        raise NotImplementedError(
            "Todo Handler deve implementar o método process()."
        )