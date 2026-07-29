from Logger import Logger
from Memoria import Memory
from InputMenager import InputManager
from ComandProcessor import CommandProcessor


def testar_logger():
    logger = Logger()

    logger.info("Sistema iniciado.")
    logger.warning("Memória quase cheia.")
    logger.error("Falha ao carregar módulo.")


def testar_memoria():
    memoria = Memory()

    memoria.start()

    memoria.save("nome", "Christyan")

    print(memoria.load("nome"))

    memoria.stop()


def testar_input():
    input_manager = InputManager()

    texto = input_manager.get_input()

    print(texto)


def testar_command_processor():
    input_manager = InputManager()
    processor = CommandProcessor()

    texto = input_manager.get_input()

    resultado = processor.process(texto)

    print(resultado)


if __name__ == "__main__":
    testar_logger()