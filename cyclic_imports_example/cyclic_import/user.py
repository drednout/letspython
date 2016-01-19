class User(object):
    STANDARD_GAMER = 0
    MODERATOR = 1
    ADMIN = 2

    def get_user(self, user_type):
        import user_fabric
        user = user_fabric.UserFactory.create_user(user_type=user_type)
        return user
