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
    테스트용 API - GET
    :param code:
    :return:
    """
    try:
        logger.info(f'get_index_v1 code : {code}')
        sample = Sample('SUCC', 'Welcome to OpenAPI')
        logger.info(f'config : {common_config.get_config(current_app.config.get("APP_ENV"))}')
        if code == 204:
            result = NoContent('조회 결과가 없습니다.').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 404:
            result = NotFound('사용자 정보 조회 결과 없음').to_tuple()
            logger.error(f'get_index_v1 ERROR : {result}')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        logger.error(f'get_index_v1 ERROR : {result}')
        err_log(logger, e, 'get_index_v1')
    return result


def post_index_v1(code, sample_body):
    """
    테스트용 API - POST
    :param code:
    :param sample_body:
    :return:
    """
    try:
        logger.info(f'post_index_v1 code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        logger.info(f'config : {common_config.get_config(current_app.config.get("APP_ENV"))}')
        if code == 204:
            result = NoContent('조회 결과가 없습니다.').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 404:
            result = NotFound('사용자 정보 조회 결과 없음').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 409:
            result = Conflict(error_code='DUPLICATE', detail='자료 중복').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        logger.error(f'post_index_v1 ERROR : {result}')
        err_log(logger, e, 'post_index_v1')
    return result


def put_index_v1(code, sample_body):
    """
    테스트용 API - PUT
    :param code:
    :param sample_body:
    :return:
    """
    try:
        logger.info(f'put_index_v1 code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        logger.info(f'config : {common_config.get_config(current_app.config.get("APP_ENV"))}')
        if code == 201:
            result = Created('Succss').to_tuple()
            logger.info(f'put_index_v1 Created : {result}')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            logger.error(f'put_index_v1 ERROR : {result}')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            logger.error(f'put_index_v1 ERROR : {result}')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            logger.error(f'put_index_v1 ERROR : {result}')
        elif code == 409:
            result = Forbidden(error_code='DUPLICATE', detail='자료 중복').to_tuple()
            logger.error(f'put_index_v1 ERROR : {result}')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        logger.error(f'put_index_v1 ERROR : {result}')
        err_log(logger, e, 'put_index_v1')
    return result


def delete_index_v1(code, sample_body=None):
    """
    테스트용 API - DELETE
    :param code:
    :param sample_body:
    :return:
    """
    try:
        logger.info(f'post_index_v1 code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        logger.info(f'config : {common_config.get_config(current_app.config.get("APP_ENV"))}')
        if code == 204:
            result = NoContent('데이터가 존재하지 않습니다.(삭제 완료 포함)').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 404:
            result = NotFound('삭제할 데이터가 없습니다.').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 409:
            result = Conflict(error_code='CONFLICT', detail='삭제할 수 없는 상태 입니다.').to_tuple()
            logger.error(f'post_index_v1 ERROR : {result}')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        logger.error(f'post_index_v1 ERROR : {result}')
        err_log(logger, e, 'post_index_v1')
    return result
