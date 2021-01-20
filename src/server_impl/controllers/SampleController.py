import logging

from flask import current_app

from openapi_test.models.sample import Sample
from .HttpStatus import *
from ..config.config import CommonConfig
from ..service.LogService import *

logger = logging.getLogger('flask-openapi-test.SampleController')
common_config_obj = CommonConfig()
common_config = None


def get_index_v1(code):
    """
    테스트용 API - GET
    :param code:
    :return:
    """
    try:
        global common_config
        common_config = common_config_obj.get_config(current_app.config.get("APP_ENV"))
        debug_log(logger, f'config : {common_config}', 'get_index_v1')
        debug_log(logger, f'code : {code}', 'get_index_v1')
        sample = Sample('SUCC', 'Welcome to OpenAPI')
        if code == 204:
            result = NoContent('조회 결과가 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'get_index_v1')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'get_index_v1')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'get_index_v1')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'get_index_v1')
        elif code == 404:
            result = NotFound('사용자 정보 조회 결과 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'get_index_v1')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        debug_log(logger, f'ERROR : {result}', 'get_index_v1')
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
        global common_config
        common_config = common_config_obj.get_config(current_app.config.get("APP_ENV"))
        debug_log(logger, f'config : {common_config}', 'get_index_v1')
        debug_log(logger, f'code, sample_body : {code}, {sample_body}', 'post_index_v1')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 204:
            result = NoContent('조회 결과가 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 404:
            result = NotFound('사용자 정보 조회 결과 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 409:
            result = Conflict(error_code='DUPLICATE', detail='자료 중복').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'post_index_v1')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        debug_log(logger, f'ERROR : {result}', 'post_index_v1')
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
        global common_config
        common_config = common_config_obj.get_config(current_app.config.get("APP_ENV"))
        debug_log(logger, f'config : {common_config}', 'get_index_v1')
        debug_log(logger, f'code, sample_body : {code}, {sample_body}', 'put_index_v1')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 201:
            result = Created('Succss').to_tuple()
            debug_log(logger, f'Created : {result}', 'put_index_v1')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'put_index_v1')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'put_index_v1')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'put_index_v1')
        elif code == 409:
            result = Forbidden(error_code='DUPLICATE', detail='자료 중복').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'put_index_v1')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        debug_log(logger, f'ERROR : {result}', 'put_index_v1')
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
        global common_config
        common_config = common_config_obj.get_config(current_app.config.get("APP_ENV"))
        debug_log(logger, f'config : {common_config}', 'get_index_v1')
        debug_log(logger, f'code, sample_body : {code}, {sample_body}', 'delete_index_v1')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 204:
            result = NoContent('데이터가 존재하지 않습니다.(삭제 완료 포함)').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 400:
            result = BadRequest('필수값이 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 401:
            result = Unauthorized(error_code='USER_NOT_FOUND', detail='사용자 정보 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 403:
            result = Forbidden(error_code='ROLE_ERROR', detail='접근 권한 없음').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 404:
            result = NotFound('삭제할 데이터가 없습니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 409:
            result = Conflict(error_code='CONFLICT', detail='삭제할 수 없는 상태 입니다.').to_tuple()
            debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        elif code == 500:
            raise Exception('오류발생')
        else:
            result = Success().to_tuple(sample)
    except Exception as e:
        result = ServerError(detail=f'{e}', error_code='UNKNOWN', error_args=f'{e.args}').to_tuple()
        debug_log(logger, f'ERROR : {result}', 'delete_index_v1')
        err_log(logger, e, 'delete_index_v1')
    return result
