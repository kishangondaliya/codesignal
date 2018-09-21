
def phoneCall(min1, min2_10, min11, s):
        if s < min1:
                return 0
        if s == min1:
                return 1
        new_s = s - min1
        max_min = 1
        i = 0
        while i < 9:
                new_s -= min2_10
                if new_s < 0:
                        return 1 + i
                i += 1
        if new_s < min11:
                return 1 + i
        if new_s <= 0:
                return 1 + i
        else:
                j = 0
                while new_s > 0:
                        new_s -= min11
                        if new_s < 0:
                                return 10 + j
                        j+=1
                return 10 + j
