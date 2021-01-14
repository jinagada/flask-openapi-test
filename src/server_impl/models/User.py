class User:
    user_id = ''
    name = ''
    display_name = ''
    email = ''

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'display_name': self.display_name,
            'email': self.email
        }
