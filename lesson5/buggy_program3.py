def is_nickname_free(user_nicknames, newNickname):
    isFree = True
    for nick in user_nicknames:
        if nick == newNickname:
            isFree = False

    return isFree


if __name__ == "__main__":
    user_nicknames = ["Vasya", "Petya", "Alex", "monster"]
    assert is_nickname_free(user_nicknames, "Vasya") == False
    assert is_nickname_free(user_nicknames, "Test") == True

