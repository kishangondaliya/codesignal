def repetitionEncryption(letter):
    pattern = r"(\w+)[^a-zA-Z]+\1\b"
    regex = re.compile(pattern, re.IGNORECASE)
    return len(re.findall(regex, letter))
