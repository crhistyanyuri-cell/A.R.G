from Config import Config
from Logger import Logger

from Memoria import Memory
from MemoryManager import MemoryManager

from ContextManager import ContextManager

from Learning import Learning
from LearningManager import LearningManager

from HandlerManager import HandlerManager

from Module_Menager import ModuleManager

from InputMenager import InputManager
from ComandProcessor import CommandProcessor

from Brain import Brain

from Core import Core


class Bootstrap:

    def build(self):

        manager = ModuleManager()


        # ==========================
        # Config
        # ==========================

        config = Config()

        manager.register(
            "config",
            config
        )


        # ==========================
        # Logger
        # ==========================

        logger = Logger(config)

        manager.register(
            "logger",
            logger
        )


        # ==========================
        # Memória
        # ==========================

        memory = Memory()

        manager.register(
            "memory",
            memory
        )


        memory_manager = MemoryManager(
            memory
        )

        manager.register(
            "memory_manager",
            memory_manager
        )


        # ==========================
        # Contexto
        # ==========================

        manager.register(

            "context",

            ContextManager()

        )


        # ==========================
        # Aprendizado
        # ==========================

        learning = Learning(
            memory_manager
        )

        manager.register(
            "learning",
            learning
        )

        manager.register(

            "learning_manager",

            LearningManager(
                learning
            )

        )


        # ==========================
        # Handlers
        # ==========================

        manager.register(

            "handler_manager",

            HandlerManager()

        )


        # ==========================
        # Entrada
        # ==========================

        manager.register(

            "input",

            InputManager()

        )


        manager.register(

            "processor",

            CommandProcessor()

        )


        # ==========================
        # Brain
        # ==========================

        manager.register(

            "brain",

            Brain()

        )


        return Core(manager)