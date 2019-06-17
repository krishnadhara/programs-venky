import logging
format = '%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(levelno)d - %(message)s'
logging.basicConfig(format=format, level=logging.DEBUG)
logger = logging.getLogger()
handler = logging.FileHandler("loki.log",mode="a")
handler.setLevel(logging.DEBUG)
shandler = logging.StreamHandler()
formatter = logging.Formatter(format)
handler.setFormatter(formatter)
shandler.setFormatter(formatter)
logger.addHandler(handler)
logger.info("reading the data from the data base")
result = {"venky":30,"loki":35}
logging.debug("result is: %s",result)
logger.info("closing the data base")

