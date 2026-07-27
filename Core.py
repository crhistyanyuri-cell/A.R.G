from Config import Config
from Logger import Logger
from Memoria import Memory
from Module_Menager import ModuleManager


class Core:

    def __init__(self):

        # Gerenciador de módulos
        self.manager = ModuleManager()

        # Registra os módulos existentes
        self.manager.register("config", Config())
        self.manager.register("logger", Logger())
        self.manager.register("memory", Memory())

        # Estado da IA
        self.running = False

    def start(self):

        self.running = True

        # Obtém os módulos necessários
        config = self.manager.get("config")
        logger = self.manager.get("logger")
        memory = self.manager.get("memory")

        # Inicia os módulos
        logger.info("Inicializando módulos...")
        memory.start()

        # Informações da IA
        name = config.get("name")
        version = config.get("version")

        print("=" * 40)
        print(f"{name} v{version}")
        print("Sistema iniciado com sucesso.")
        print("=" * 40)

        logger.info("Sistema iniciado.")

    def stop(self):

        # Obtém os módulos
        logger = self.manager.get("logger")
        memory = self.manager.get("memory")

        # Encerra os módulos
        memory.stop()
        logger.info("Sistema encerrado.")

        self.running = False

        print("=" * 40)
        print("Sistema encerrado.")
        print("=" * 40)