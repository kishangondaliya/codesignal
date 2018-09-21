def transposeDictionary(scriptByExtension):
    return [ [x[1], x[0]] for x in sorted(scriptByExtension.items(), key=lambda x:x[1])]
