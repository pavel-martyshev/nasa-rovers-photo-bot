from loguru import logger


# noinspection PyUnusedLocal
def my_filter(record):
    return True


logger.remove()
logger.add('log/{time:%d-%m-%Y}.log', level='DEBUG', rotation='00:00',
           format='{time:%H:%M:%S}: {level} - {message}', filter=my_filter)
lg = logger
