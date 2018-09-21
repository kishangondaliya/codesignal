def countVowelConsonant(s):
    sum = 0
    for e in s:
        if e in ['a','e','i','o','u']:
           sum += 1
        else:
            sum += 2
    return sum

