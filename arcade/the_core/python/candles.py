def candles(candlesNumber, makeNew):
    left_o = 0
    burned = 0
    while candlesNumber > 0:
        candlesNumber -= 1
        left_o += 1
        if left_o == makeNew:
            candlesNumber += 1
            left_o = 0
        burned += 1
    return burned
