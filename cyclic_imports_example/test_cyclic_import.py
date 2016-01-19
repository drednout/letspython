import cyclic_import.moderator_user as moderator_user
import cyclic_import.standard_gamer as standard_gamer


moder = moderator_user.ModeratorUser()
simple_user = standard_gamer.StandardGamer()
simple_user2 = moder.get_user(moder.STANDARD_GAMER)

