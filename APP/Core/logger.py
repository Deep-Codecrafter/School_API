import logging

logging.basicConfig(filename="app.log",
                    filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG,)

class logger:
    @staticmethod
    def cri(message:str):
        logging.critical(message)

    @staticmethod
    def Deb(message:str):
        logging.debug(message)

    @staticmethod
    def io(message:str):
        logging.info(message)

    @staticmethod
    def errr(message:str):
        logging.error(message)

    @staticmethod
    def war(message:str):
        logging.warning(message)