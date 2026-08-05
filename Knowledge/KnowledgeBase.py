class KnowledgeBase:


    def __init__(self):

        self.knowledge = {


            # ==========================
            # Ciência
            # ==========================

            "estrela":

                "Uma estrela é um corpo celeste que produz sua própria energia através de reações de fusão nuclear em seu núcleo.",


            "planeta":

                "Um planeta é um corpo celeste que orbita uma estrela e possui massa suficiente para assumir uma forma aproximadamente esférica.",



            # ==========================
            # Tecnologia
            # ==========================

            "computador":

                "Um computador é uma máquina capaz de receber, processar, armazenar e transmitir informações através de componentes eletrônicos e software."

        }



    # =====================================
    # Buscar conhecimento
    # =====================================

    def search(self, termo):

        termo = termo.lower()


        for chave, resposta in self.knowledge.items():

            if chave in termo:

                return resposta


        return None



    # =====================================
    # Adicionar conhecimento
    # =====================================

    def add(self, chave, resposta):

        self.knowledge[chave.lower()] = resposta



    # =====================================
    # Listar conhecimento
    # =====================================

    def get_all(self):

        return self.knowledge