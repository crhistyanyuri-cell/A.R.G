from Config import Config
from Logger import Logger

from Memoria import Memory
from MemoryManager import MemoryManager

from Learning import Learning
from LearningManager import LearningManager

from ContextManager import ContextManager

from Module_Menager import ModuleManager

from InputMenager import InputManager
from ComandProcessor import CommandProcessor

from Brain import Brain


class Core:

    def __init__(self):

        # Gerenciador de módulos
        self.manager = ModuleManager()

        # Registra todos os módulos
        self._register_modules()

        # Estado da IA
        self.running = False


    def _register_modules(self):

        # Configuração
        config = Config()

        # Logger
        logger = Logger(config)

        # Memória
        memory = Memory()

        # Gerenciador da memória
        memory_manager = MemoryManager(
            memory
        )

        # Aprendizado
        learning = Learning(
            memory_manager
        )

        learning_manager = LearningManager(
            learning
        )

        # Contexto
        context = ContextManager()

        # Entrada
        input_manager = InputManager()

        # Processador
        processor = CommandProcessor()

        # Cérebro
        brain = Brain()

        # Registro dos módulos
        self.manager.register(
            "config",
            config
        )

        self.manager.register(
            "logger",
            logger
        )

        self.manager.register(
            "memory",
            memory
        )

        self.manager.register(
            "memory_manager",
            memory_manager
        )

        self.manager.register(
            "learning",
            learning
        )

        self.manager.register(
            "learning_manager",
            learning_manager
        )

        self.manager.register(
            "context",
            context
        )

        self.manager.register(
            "input",
            input_manager
        )

        self.manager.register(
            "processor",
            processor
        )

        self.manager.register(
            "brain",
            brain
        )


    def start(self):

        self.running = True

        logger = self.manager.get("logger")
        memory = self.manager.get("memory")
        config = self.manager.get("config")

        logger.info("Inicializando módulos...")

        memory.start()

        print("=" * 40)
        print(f"{config.get('name')} v{config.get('version')}")
        print("Sistema iniciado com sucesso.")
        print("=" * 40)

        logger.info("Sistema iniciado.")


    def run(self):

        logger = self.manager.get("logger")
        input_manager = self.manager.get("input")
        processor = self.manager.get("processor")
        brain = self.manager.get("brain")

        logger.info("Aguardando comandos...")

        while self.running:

            texto = input_manager.get_input()

            resultado = processor.process(
                texto
            )

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

                            print(
                                f"{chave}: {valor}"
                            )

                    else:

                        print(
                            "Memória vazia."
                        )

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

                        print(
                            "Histórico vazio."
                        )

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


    def stop(self):

        logger = self.manager.get("logger")
        memory = self.manager.get("memory")

        memory.stop()

        logger.info(
            "Sistema encerrado."
        )

        self.running = False

        print("=" * 40)
        print("Sistema encerrado.")
        print("=" * 40)