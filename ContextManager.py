class ContextManager:

    def __init__(self):

        self.clear()


    # ==========================
    # Métodos básicos
    # ==========================

    def set(self, key, value):

        self.context[key] = value


    def get(self, key):

        return self.context.get(key)


    # ==========================
    # Intenções
    # ==========================

    def update_intent(self, intent):

        self.context["last_intent"] = self.context["intent"]
        self.context["intent"] = intent


    # ==========================
    # Histórico
    # ==========================

    def add_history(self, user_message, response, intent):

        self.context["history"].append({

            "user": user_message,
            "intent": intent,
            "response": response

        })


    def get_history(self):

        return self.context["history"]


    def clear_history(self):

        self.context["history"].clear()


    # ==========================
    # Contexto
    # ==========================

    def clear(self):

        self.context = {

            # Mensagem
            "message": None,
            "original_message": None,

            # Intenções
            "intent": None,
            "last_intent": None,

            # Respostas
            "last_response": None,
            "current_handler": None,

            # Conversa
            "last_topic": None,

            # Histórico
            "history": []

        }