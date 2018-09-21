def growingPlant(upSpeed, downSpeed, desiredHeight):
    size = 0
    day = 1
    while size < desiredHeight:
        size += upSpeed
        if size >= desiredHeight:
            return day
        size -= downSpeed
        day += 1
    return day 
