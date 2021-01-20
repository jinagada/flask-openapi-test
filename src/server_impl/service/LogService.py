def err_log(logger, e, fn_name):
    """
    오류로그 출력
    :param logger:
    :param e:
    :param fn_name:
    """
    logger.error(f'{fn_name} Exception : {e}')
    logger.error(f'{fn_name} Exception args : {e.args}')


def debug_log(logger, msg, fn_name):
    """
    디버그로그 출력
    :param logger:
    :param msg:
    :param fn_name:
    """
    logger.debug(f'{fn_name} {msg}')
