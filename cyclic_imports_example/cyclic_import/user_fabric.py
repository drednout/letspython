import standard_gamer
import moderator_user


class UserFactory(object):
    @staticmethod
    def create_user(user_type):
        if user_type == standard_gamer.StandardGamer.STANDARD_GAMER:
            return standard_gamer.StandardGamer()
        elif user_type == moderator_user.ModeratorUser.MODERATOR:
            return moderator_user.ModeratorUser()
