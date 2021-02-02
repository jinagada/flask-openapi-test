class ApiServerException(Exception):
    """
    임의로 오류를 발생시킬 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지}, {응답코드, 오류코드 등}, {응답상세, 오류상세 등} 순서로 파라메터 작성
        :param args:
        """
        self.msg = args[0]
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self.msg


class DataNotFoundException(Exception):
    """
    조회 결과가 없는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : 데이터가 없는 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'Data Not Found.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class DataDuplicationException(Exception):
    """
    중복 데이터가 있는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : 중복 데이터가 있는 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'Duplicated Data.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class DataErrorException(Exception):
    """
    데이터에 문제가 있는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : 데이터에 문제가 있는 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'Data Error.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class BadParameterException(Exception):
    """
    Parameter에 오류가 있는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : Parameter에 오류가 있는 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'Bad Parameters.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class UnauthorizedUserException(Exception):
    """
    User가 인증되지 않은 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : User가 인증되지 않은 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'Unauthorized User.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class UserPermissionException(Exception):
    """
    User가 권한이 없는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : User가 권한이 없는 경우 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'No Permission.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg


class UserNotFoundException(Exception):
    """
    User가 없는 경우 사용하는 Exception class
    """

    def __init__(self, *args):
        """
        {오류메시지} : User가 없는 경우 사용할 메시지
        :param args:
        """
        if args[0]:
            self._msg = args[0]
        else:
            self._msg = 'User Not Found.'
        super().__init__(*args)

    def __str__(self):
        """
        생성시 작성된 첫번째 파라메터인 {오류메시지}를 반환
        :return:
        """
        return self._msg
