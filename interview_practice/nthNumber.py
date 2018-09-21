def nthNumber(s, n):
    pattern = r"[^1-9]*[1-9]+[0-9]*[^1-9]*" * (n-1) + r"[^1-9]*([1-9]+[0-9]*)[^1-9]*"
    return re.match(pattern, s).group(1)
