def killKthBit(n, k):
    return int("".join(list(bin(n)[2:])[:-k] +["0"]+ list(bin(n)[2:])[len(bin(n))-k-1:]),2)


# should look at : https://stackoverflow.com/questions/40483029/java-setting-a-distinct-bit-of-an-integer-to-zero
