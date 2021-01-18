class CommonConfig:
    def __init__(self):
        """
        개발용 설정
        """
        self.dev_config = {
            'db_config': {
                'db_name': {
                    'host': 'dev'
                }
            }
        }

        """
        운영용 설정
        """
        self.prd_config = {
            'db_config': {
                'db_name': {
                    'host': 'dev'
                }
            }
        }

    def get_config(self, env):
        """
        env 값에 해당하는 설정 dict 반환
        :param env:
        :return:
        """
        config_obj = None
        if env == 'dev':
            config_obj = self.dev_config
        elif env == 'prd':
            config_obj = self.prd_config
        return config_obj
