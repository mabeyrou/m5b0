from loguru import logger

def square(integer: int):
    if not isinstance(integer, int):
        logger.error(f'{integer} is not an integer.')
        raise TypeError('It must be an integer.')
    return integer**2