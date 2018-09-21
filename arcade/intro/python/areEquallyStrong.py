def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    return (yourLeft == friendsLeft or yourLeft == friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight)
