class Config(object):
    DEBUG = False
    TESTING = False
    CREATE_TEST_DATABASE = False
    DB_URL = 'dev'


class ProductionConfig(Config):
    DB_URL = 'prd'


class DevelopmentConfig(Config):
    DEBUG = True
    CREATE_TEST_DATABASE = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    CREATE_TEST_DATABASE = True
