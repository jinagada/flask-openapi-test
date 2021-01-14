from ..models.User import User
from openapi_test.models.user import User as User1
import logging


def get_user(user_id):
    logger = logging.getLogger('flask-openapi-test.UsersController')
    logger.info(f'user_id : {user_id}')
    if user_id == 'test':
        user = User()
        user.user_id = user_id
        user.name = '테스트명'
        user.display_name = '별명'
        user.email = 'test@test.com'
    else:
        user = User1()
        user.user_id = user_id
        user.name = f'{user_id}님'
        user.display_name = f'{user_id}별명'
        user.email = f'{user_id}@test.com'
    return user.to_dict()
