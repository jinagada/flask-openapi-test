import logging

from flask import current_app

from openapi_test.models.sample import Sample
from .HttpStatus import *
from ..config.config import CommonConfig
from ..service.LogService import err_log

logger = logging.getLogger('flask-openapi-test.SampleController')
common_config = CommonConfig()


def get_index_v1(code):
    """
    테스트용 API
    :param code:
    :return:
    """
    try:
        sample = Sample()
        sample.code = 'SUCC'
        sample.message = 'Welcome to OpenAPI'
        logger.info(f'Welcome Url Request : {sample}')
        logger.info(f'config : {common_config.get_config(current_app.config.get("APP_ENV"))}')
        if code == 204:
            result = NoContent('조회 결과가 없습니다.').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 400:
            result = BadRequest(error_code='PARAM_ERR', error_message='필수값이 없습니다.').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', error_message='사용자 정보 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', error_message='접근 권한 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 404:
            result = NotFound(message='User Info Not Found', error_code='NO_DATA',
                              error_message='사용자 정보 조회 결과 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = sample.to_dict(), 200
    except Exception as e:
        result = ServerError(message='Server Error', error_code='UNKNOWN',
                             error_message=f'{e}').to_tuple()
        logger.error(f'get_index_v1 ERROR : {result}')
        err_log(logger, e, 'get_index_v1')
    return result
