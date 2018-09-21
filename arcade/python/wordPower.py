def wordPower(word):
    num = {key: string.ascii_lowercase.find(key)+1 for key in word}
    return sum([num[ch] for ch in word])
