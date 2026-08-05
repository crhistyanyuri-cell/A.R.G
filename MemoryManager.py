class MemoryManager:

    def __init__(self, memory):

        self.memory = memory


    # ==========================
    # Métodos genéricos
    # ==========================

    def save(self, key, value):

        self.memory.save(
            key,
            value
        )


    def load(self, key, default=None):

        value = self.memory.load(key)

        if value is None:

            return default

        return value


    def delete(self, key):

        self.memory.delete(
            key
        )


    # ==========================
    # USUÁRIO
    # ==========================

    def set_user_name(self, name):

        self.save(
            "user_name",
            name
        )


    def get_user_name(self):

        return self.load(
            "user_name"
        )


    def delete_user_name(self):

        self.delete(
            "user_name"
        )


    # ==========================
    # PREFERÊNCIAS
    # ==========================

    def set_preference(self, key, value):

        preferences = self.load(
            "preferences",
            {}
        )

        preferences[key] = value

        self.save(
            "preferences",
            preferences
        )


    def get_preference(self, key):

        preferences = self.load(
            "preferences",
            {}
        )

        return preferences.get(key)


    # ==========================
    # FATOS
    # ==========================

    def add_fact(self, fact):

        facts = self.load(
            "facts",
            []
        )

        if fact not in facts:

            facts.append(fact)

            self.save(
                "facts",
                facts
            )


    def get_facts(self):

        return self.load(
            "facts",
            []
        )


    # ==========================
    # PERFIL
    # ==========================

    def get_profile(self):

        return {

            "user_name":

                self.get_user_name(),

            "preferences":

                self.load(
                    "preferences",
                    {}
                ),

            "facts":

                self.load(
                    "facts",
                    []
                )

        }