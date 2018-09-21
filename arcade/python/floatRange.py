# from itertools import islice, count

# def floatRange(start, stop, step):
#     gen =  [] if start == stop else (round(i, 3 ) for i in islice(count(start, step), ((stop - start) // step)+1))
#     return list(gen)


from itertools import count, takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)
