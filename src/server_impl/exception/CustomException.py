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
