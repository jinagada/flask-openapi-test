import logging
import traceback

from flask import current_app

from openapi_test.models.sample import Sample
from .HttpStatus import *
from ..config.config import CommonConfig
from ..exception.CustomException import *
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
        debug_log(logger, 'get_index_v1', f'config : {common_config}')
        debug_log(logger, 'get_index_v1', f'code : {code}')
        sample = Sample('SUCC', 'Welcome to OpenAPI')
        if code == 204:
            raise DataNotFoundException('조회 결과가 없습니다.')
        if code == 400:
            raise BadParameterException('필수값이 없습니다.')
        if code == 401:
            raise UnauthorizedUserException('인증되지 않은 사용자입니다.')
        if code == 403:
            raise UserPermissionException('접근 권한 없음')
        if code == 404:
            raise UserNotFoundException('사용자 정보 조회 결과 없음')
        if code == 500:
            raise ApiServerException('서버 오류 발생', 'E01', '테스트용 오류 강제 생성')
        result = Success().to_tuple(sample)
    except DataNotFoundException as e:
        result = NoContent(str(e)).to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
    except BadParameterException as e:
        result = BadRequest(str(e)).to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
    except UnauthorizedUserException as e:
        result = Unauthorized(str(e)).to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
    except UserPermissionException as e:
        result = Forbidden(str(e)).to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
    except UserNotFoundException as e:
        result = NotFound(str(e)).to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
    except Exception as e:
        result = ServerError(f'{e}').to_tuple()
        err_log(logger, 'get_index_v1', e, traceback.format_exc())
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
        debug_log(logger, 'post_index_v1', f'config : {common_config}')
        debug_log(logger, 'post_index_v1', f'code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 204:
            raise DataNotFoundException('조회 결과가 없습니다.')
        if code == 400:
            raise BadParameterException('필수값이 없습니다.')
        if code == 401:
            raise UnauthorizedUserException('인증되지 않은 사용자입니다.')
        if code == 403:
            raise UserPermissionException('접근 권한 없음')
        if code == 404:
            raise UserNotFoundException('사용자 정보 조회 결과 없음')
        if code == 409:
            raise DataDuplicationException('자료 중복')
        if code == 500:
            raise ApiServerException('서버 오류 발생', 'E01', '테스트용 오류 강제 생성')
        result = Success().to_tuple(sample)
    except DataNotFoundException as e:
        result = NoContent(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except BadParameterException as e:
        result = BadRequest(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except UnauthorizedUserException as e:
        result = Unauthorized(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except UserPermissionException as e:
        result = Forbidden(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except UserNotFoundException as e:
        result = NotFound(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except DataDuplicationException as e:
        result = Conflict(str(e)).to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
    except Exception as e:
        result = ServerError(f'{e}').to_tuple()
        err_log(logger, 'post_index_v1', e, traceback.format_exc())
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
        debug_log(logger, 'put_index_v1', f'config : {common_config}')
        debug_log(logger, 'put_index_v1', f'code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 400:
            raise BadParameterException('필수값이 없습니다.')
        if code == 401:
            raise UnauthorizedUserException('인증되지 않은 사용자입니다.')
        if code == 403:
            raise UserPermissionException('접근 권한 없음')
        if code == 409:
            raise DataDuplicationException('자료 중복')
        if code == 500:
            raise ApiServerException('서버 오류 발생', 'E01', '테스트용 오류 강제 생성')
        if code == 201:
            result = Created('Succss').to_tuple()
            debug_log(logger, 'put_index_v1', f'Created : {result}')
        else:
            result = Success().to_tuple(sample)
    except BadParameterException as e:
        result = BadRequest(str(e)).to_tuple()
        err_log(logger, 'put_index_v1', e, traceback.format_exc())
    except UnauthorizedUserException as e:
        result = Unauthorized(str(e)).to_tuple()
        err_log(logger, 'put_index_v1', e, traceback.format_exc())
    except UserPermissionException as e:
        result = Forbidden(str(e)).to_tuple()
        err_log(logger, 'put_index_v1', e, traceback.format_exc())
    except DataDuplicationException as e:
        result = Conflict(str(e)).to_tuple()
        err_log(logger, 'put_index_v1', e, traceback.format_exc())
    except Exception as e:
        result = ServerError(f'{e}').to_tuple()
        err_log(logger, 'put_index_v1', e, traceback.format_exc())
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
        debug_log(logger, 'delete_index_v1', f'config : {common_config}')
        debug_log(logger, 'delete_index_v1', f'code, sample_body : {code}, {sample_body}')
        sample = Sample(sample_body.code, sample_body.message)
        if code == 204:
            raise DataNotFoundException('데이터가 존재하지 않습니다.(삭제 완료 포함)')
        if code == 400:
            raise BadParameterException('필수값이 없습니다.')
        if code == 401:
            raise UnauthorizedUserException('인증되지 않은 사용자입니다.')
        if code == 403:
            raise UserPermissionException('접근 권한 없음')
        if code == 404:
            raise UserNotFoundException('삭제할 데이터가 없습니다.')
        if code == 409:
            raise DataErrorException('삭제할 수 없는 상태 입니다.')
        if code == 500:
            raise ApiServerException('서버 오류 발생', 'E01', '테스트용 오류 강제 생성')
        result = Success().to_tuple(sample)
    except DataNotFoundException as e:
        result = NoContent(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except BadParameterException as e:
        result = BadRequest(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except UnauthorizedUserException as e:
        result = Unauthorized(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except UserPermissionException as e:
        result = Forbidden(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except UserNotFoundException as e:
        result = NotFound(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except DataErrorException as e:
        result = Conflict(str(e)).to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    except Exception as e:
        result = ServerError(f'{e}').to_tuple()
        err_log(logger, 'delete_index_v1', e, traceback.format_exc())
    return result
