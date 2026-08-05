from Intent.IntentTypes import IntentTypes


class LearningManager:

    def __init__(self, learning):

        self.learning = learning

        self.actions = {

            IntentTypes.REMEMBER_USER_NAME:
                self.learning.remember_name,

            # Futuramente:
            # IntentTypes.REMEMBER_USER_AGE:
            #     self.learning.remember_age,

            # IntentTypes.REMEMBER_USER_CITY:
            #     self.learning.remember_city,
        }


    def process(self, intent, data):

        # ==========================
        # Dados simples
        # ==========================

        action = self.actions.get(intent)

        if action is not None:

            action(data)

            return True


        # ==========================
        # Fatos
        # ==========================

        if intent == IntentTypes.LEARN_FACT:

            self.learning.learn_fact(
                data
            )

            return True


        # ==========================
        # Preferências
        # ==========================

        if intent == IntentTypes.LEARN_PREFERENCE:

            self.learning.learn_preference(

                data["key"],

                data["value"]

            )

            return True


        return False