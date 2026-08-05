class MemoryManager:

    def __init__(self, memory):

        self.memory = memory


    # ==========================
    # USUÁRIO
    # ==========================

    def set_user_name(self, name):

        self.memory.save(
            "user_name",
            name
        )


    def get_user_name(self):

        return self.memory.load(
            "user_name"
        )


    def delete_user_name(self):

        self.memory.delete(
            "user_name"
        )


    # ==========================
    # PREFERÊNCIAS
    # ==========================

    def set_preference(self, key, value):

        preferences = self.memory.load(
            "preferences"
        )

        if preferences is None:

            preferences = {}

        preferences[key] = value

        self.memory.save(
            "preferences",
            preferences
        )


    def get_preference(self, key):

        preferences = self.memory.load(
            "preferences"
        )

        if preferences is None:

            return None

        return preferences.get(key)


    # ==========================
    # FATOS
    # ==========================

    def add_fact(self, fact):

        facts = self.memory.load(
            "facts"
        )

        if facts is None:

            facts = []

        if fact not in facts:

            facts.append(fact)

            self.memory.save(
                "facts",
                facts
            )


    def get_facts(self):

        facts = self.memory.load(
            "facts"
        )

        if facts is None:

            return []

        return facts


    # ==========================
    # PERFIL
    # ==========================

    def get_profile(self):

        return {

            "user_name": self.get_user_name(),

            "preferences":

                self.memory.load(
                    "preferences"
                ) or {},

            "facts":

                self.memory.load(
                    "facts"
                ) or []

        }