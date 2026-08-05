def run(self):

    logger = self.manager.get("logger")
    input_manager = self.manager.get("input")
    processor = self.manager.get("processor")
    brain = self.manager.get("brain")

    logger.info("Aguardando comandos...")

    while self.running:

        texto = input_manager.get_input()

        resultado = processor.process(texto)

        if resultado["type"] == "command":

            comando = resultado["content"]


            # ==========================
            # ENCERRAR
            # ==========================

            if comando == "sair":

                logger.info(
                    "Encerrando sistema..."
                )

                self.running = False


            # ==========================
            # MEMÓRIA
            # ==========================

            elif comando == "memory":

                memory = self.manager.get(
                    "memory"
                )

                print("")
                print("===== MEMÓRIA =====")

                dados = memory.get_all()

                if dados:

                    for chave, valor in dados.items():

                        print(f"{chave}: {valor}")

                else:

                    print("Memória vazia.")

                print("===================")
                print("")


            # ==========================
            # HISTÓRICO
            # ==========================

            elif comando == "history":

                context = self.manager.get(
                    "context"
                )

                print("")
                print("===== HISTÓRICO =====")

                historico = context.get(
                    "history"
                )

                if historico:

                    for item in historico:

                        print(item)

                else:

                    print("Histórico vazio.")

                print("====================")
                print("")


            # ==========================
            # AJUDA
            # ==========================

            elif comando == "help":

                print("")
                print("===== COMANDOS =====")
                print("/help")
                print("/memory")
                print("/history")
                print("/sair")
                print("====================")
                print("")


            # ==========================
            # DESCONHECIDO
            # ==========================

            else:

                logger.warning(
                    f"Comando desconhecido: {comando}"
                )


        elif resultado["type"] == "message":

            resposta = brain.think(
                resultado["content"],
                self.manager
            )

            print(resposta)