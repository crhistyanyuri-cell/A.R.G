class QuestionHandler:


    def process(self, context, manager):


        message = context.get(
            "message"
        )


        if not message.startswith(
            ("o que", "quem", "como")
        ):

            return None



        knowledge = manager.get(
            "knowledge"
        )


        resposta = knowledge.search(
            message
        )


        if resposta:

            return resposta



        return None