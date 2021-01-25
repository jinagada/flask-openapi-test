from openapi_test.models.http_status_message import HttpStatusMessage


class HttpStatus:
    def __init__(self, title, status, detail, type_txt='about:blank'):
        """
        변수 설정
        :param title:
        :param status:
        :param detail:
        :param type_txt:
        """
        self.title = title
        self.status = status
        self.detail = detail
        self.type = type_txt

    def to_tuple(self):
        """
        Tuple 로 변환하여 반환
        :return:
        """
        temp_obj = HttpStatusMessage(title=self.title, status=self.status, detail=self.detail, type_txt=self.type)
        temp_dict = temp_obj.to_dict()
        temp_dict['type'] = temp_dict['type_txt']
        del temp_dict['type_txt']
        result = temp_dict
        return result, self.status


class Success(HttpStatus):
    """
    Created Retrun
    """
    def __init__(self):
        super().__init__('', 200, '')

    def to_tuple(self, result_dict=None):
        """
        Tuple 로 변환하여 반환
        :return:
        """
        if 'to_dict' in result_dict:
            result = result_dict.to_dict()
        else:
            result = result_dict
        return result, self.status


class Created(HttpStatus):
    """
    Created Retrun
    """
    def __init__(self, title):
        super().__init__(title, 201, title)


class NoContent(HttpStatus):
    """
    No Content Retrun
    """
    def __init__(self, title):
        super().__init__(title, 204, title)


class BadRequest(HttpStatus):
    """
    Bad Request Retrun
    """
    def __init__(self, detail):
        super().__init__('Bad Request', 400, detail)


class Unauthorized(HttpStatus):
    """
    Unauthorized Retrun
    """
    def __init__(self, detail=None):
        super().__init__('Unauthorized', 401, detail)


class Forbidden(HttpStatus):
    """
    Forbidden Retrun
    """
    def __init__(self, detail=None):
        super().__init__('Forbidden', 403, detail)


class NotFound(HttpStatus):
    """
    Not Found Retrun
    """
    def __init__(self, detail='Not Found'):
        super().__init__('Not Found', 404, detail)


class Conflict(HttpStatus):
    """
    Conflict Retrun
    """
    def __init__(self, detail=None):
        super().__init__('Conflict', 409, detail)


class ServerError(HttpStatus):
    """
    500 Server Error Return
    """
    def __init__(self, detail='Server Error'):
        super().__init__('Server Error', 500, detail)
