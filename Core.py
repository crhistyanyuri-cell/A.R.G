from typing import Self


class Core:


    def __init__(self, manager):

        self.manager = manager

        self.running = False



    # =====================================
    # Inicialização
    # =====================================

    def start(self):

        self.running = True


        logger = self.manager.get(
            "logger"
        )

        config = self.manager.get(
            "config"
        )


        logger.info(
            "Inicializando módulos..."
        )


        self.manager.start_all()



        print("=" * 40)

        print(
            f"{config.get('name')} v{config.get('version')}"
        )

        print(
            "Sistema iniciado com sucesso."
        )

        print("=" * 40)


        logger.info(
            "Sistema iniciado."
        )



    # =====================================
    # Loop principal
    # =====================================

    def run(self):

        logger = self.manager.get(
            "logger"
        )

        input_manager = self.manager.get(
            "input"
        )

        processor = self.manager.get(
            "processor"
        )

        brain = self.manager.get(
            "brain"
        )


        logger.info(
            "Aguardando comandos..."
        )


        while self.running:


            texto = input_manager.get_input()


            resultado = processor.process(
                texto
            )


            if resultado["type"] == "command":


                self.process_command(
                    resultado["content"]
                )


            elif resultado["type"] == "message":


                resposta = brain.think(

                    resultado["content"],

                    self.manager

                )


                print(resposta)



    # =====================================
    # Comandos
    # =====================================

    def process_command(self, comando):

        logger = self.manager.get(
            "logger"
        )


        if comando == "sair":

            logger.info(
                "Encerrando sistema..."
            )


            self.stop()

            return



        if comando == "help":

            print("")
            print("===== COMANDOS =====")
            print("/help")
            print("/memory")
            print("/history")
            print("/sair")
            print("====================")
            print("")

            return



        if comando == "memory":

            memory = self.manager.get(
                "memory"
            )


            print("")
            print("===== MEMÓRIA =====")


            dados = memory.get_all()


            if dados:

                for chave, valor in dados.items():

                    print(
                        f"{chave}: {valor}"
                    )

            else:

                print(
                    "Memória vazia."
                )


            print("===================")
            print("")

            return



        if comando == "history":

            context = self.manager.get(
                "context"
            )


            print("")
            print("===== HISTÓRICO =====")


            historico = context.get_history()


            if historico:

                for item in historico:

                    print(item)

            else:

                print(
                    "Histórico vazio."
                )


            print("====================")
            print("")

            return



        logger.warning(
            f"Comando desconhecido: {comando}"
        )



    # =====================================
    # Encerramento
    # =====================================

    def stop(self):

        if not self.running:
            return


    logger = Self.manager.get(
        "logger"
    )


    logger.info(
        "Encerrando módulos..."
    )


    Self.manager.stop_all()


    Self.running = False


    logger.info(
        "Sistema encerrado."
    )


    print("=" * 40)

    print(
        "Sistema encerrado."
    )

    print("=" * 40)