from logging import Logger


def err_log(logger: Logger, fn_name, e, traceback_str):
    """
    ERROR 로그 출력
    :param logger:
    :param e:
    :param fn_name:
    :param traceback_str:
    """
    logger.error(f'{fn_name} Exception : {e}')
    logger.error(f'{fn_name} Exception args : {e.args}')
    logger.error(traceback_str)


def debug_log(logger: Logger, fn_name, msg):
    """
    DEBUG 로그 출력
    :param logger:
    :param msg:
    :param fn_name:
    """
    logger.debug(f'{fn_name} {msg}')


def info_log(logger: Logger, fn_name, msg):
    """
    INFO 로그 출력
    :param logger:
    :param msg:
    :param fn_name:
    """
    logger.info(f'{fn_name} {msg}')
