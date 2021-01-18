from openapi_test.models.http_status_message import HttpStatusMessage


class HttpStatus:
    def __init__(self, status_code, message, error_code=None, error_message=None):
        """
        변수 설정
        :param error_code:
        :param error_message:
        """
        self.status_code = status_code
        self.message = message
        self.error_code = error_code
        self.error_message = error_message

    def to_tuple(self):
        """
        Tuple 로 변환하여 반환
        :return:
        """
        result = HttpStatusMessage(message=self.message, error_code=self.error_code, error_message=self.error_message)
        return result, self.status_code


class NoContent(HttpStatus):
    """
    Bad Request Retrun
    """
    def __init__(self, message):
        super().__init__(204, message)


class BadRequest(HttpStatus):
    """
    Bad Request Retrun
    """
    def __init__(self, error_code=None, error_message=None):
        super().__init__(400, 'Bad Request', error_code, error_message)


class Unauthorized(HttpStatus):
    """
    Unauthorized Retrun
    """
    def __init__(self, error_code=None, error_message=None):
        super().__init__(401, 'Unauthorized', error_code, error_message)


class Forbidden(HttpStatus):
    """
    Forbidden Retrun
    """
    def __init__(self, error_code=None, error_message=None):
        super().__init__(403, 'Forbidden', error_code, error_message)


class NotFound(HttpStatus):
    """
    Not Found Retrun
    """
    def __init__(self, message='Not Found', error_code=None, error_message=None):
        super().__init__(404, message, error_code, error_message)


class ServerError(HttpStatus):
    """
    500 Server Error Return
    """
    def __init__(self, message='Server Error', error_code=None, error_message=None):
        super().__init__(500, message, error_code, error_message)
