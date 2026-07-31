from Config import Config
from Logger import Logger
from Memoria import Memory
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

        config = Config()

        self.manager.register("config", config)
        self.manager.register("logger", Logger(config))
        self.manager.register("memory", Memory())
        self.manager.register("context", ContextManager())
        self.manager.register("input", InputManager())
        self.manager.register("processor", CommandProcessor())
        self.manager.register("brain", Brain())


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

            resultado = processor.process(texto)

            if resultado["type"] == "command":

                comando = resultado["content"]

                if comando == "sair":

                    logger.info("Encerrando sistema...")
                    self.running = False

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

        logger.info("Sistema encerrado.")

        self.running = False

        print("=" * 40)
        print("Sistema encerrado.")
        print("=" * 40)