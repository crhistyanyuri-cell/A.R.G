from Config import Config
from Logger import Logger

from Memoria import Memory
from MemoryManager import MemoryManager

from ContextManager import ContextManager

from Learning import Learning
from LearningManager import LearningManager

from Knowledge.KnowledgeBase import KnowledgeBase

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


        learning_manager = LearningManager(
            learning
        )

        manager.register(
            "learning_manager",
            learning_manager
        )



        # ==========================
        # Conhecimento
        # ==========================

        knowledge = KnowledgeBase()


        manager.register(

            "knowledge",

            knowledge

        )



        # ==========================
        # Handlers
        # ==========================

        handler_manager = HandlerManager()

        manager.register(

            "handler_manager",

            handler_manager

        )



        # ==========================
        # Entrada
        # ==========================

        input_manager = InputManager()

        manager.register(

            "input",

            input_manager

        )


        processor = CommandProcessor()

        manager.register(

            "processor",

            processor

        )



        # ==========================
        # Brain
        # ==========================

        brain = Brain()

        manager.register(

            "brain",

            brain

        )



        return Core(manager)