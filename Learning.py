class Learning:

    def __init__(self, memory_manager):

        self.memory = memory_manager


    # ==========================
    # Aprendizado genérico
    # ==========================

    def learn(self, key, value):

        self.memory.save(
            key,
            value
        )


    # ==========================
    # Fatos
    # ==========================

    def learn_fact(self, fact):

        self.memory.add_fact(
            fact
        )


    # ==========================
    # Preferências
    # ==========================

    def learn_preference(self, key, value):

        self.memory.set_preference(
            key,
            value
        )


    # ==========================
    # Dados do usuário
    # ==========================

    def remember_name(self, name):

        self.learn(
            "user_name",
            name
        )


    def remember_age(self, age):

        self.learn(
            "user_age",
            age
        )


    def remember_city(self, city):

        self.learn(
            "user_city",
            city
        )