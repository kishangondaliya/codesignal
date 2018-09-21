def companyBotStrategy(trainingData):
    num = 0
    cnt = 0
    for e in trainingData:
        if e[1] > 0:
            num += e[0]
            cnt += 1
    if cnt > 0:
        return num/cnt
    
    return 0.0
