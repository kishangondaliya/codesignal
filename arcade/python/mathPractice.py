from functools import reduce

def mathPractice(numbers):
    return reduce(lambda x, (i,y): x + y if i%2 else z*y, enumerate(numbers), 0)
