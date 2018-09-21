def swapAdjacentWords(s):
    return re.sub('(\w+)\s(\w+)', r'\2 \1', s)

