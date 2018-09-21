def areFollowingPatterns(strings, patterns):
    
    if len(strings) != len(patterns):
        return False
    arrs = {}
    arrp = {}
    i = 0
    test = {}
    
    while i < len(patterns):
        if patterns[i] in test:
            if test[patterns[i]] != strings[i]:
                return False
        else:
            if strings[i] in test.values():
                return False
            test[patterns[i]] = strings[i]

        i += 1
    return True
#     while i < len(strings)-1:
#         s1 = "notsame"
#         p1 = "notsame"
#         if strings[i] in arrs:
#             return False
#         if patterns[i] in arrp:
#             return False

#         if patterns[i] in test:
#             if test[patterns[i]] != strings[i]:
#                 return False
#             else:
#                 test[patterns[i]] = strings[i]
#         if strings[i] in test.values():
#             return False
    
#         if patterns[i] == patterns[i+1]:
#             p1 = "same"
#             arrp[i] = 's'
#         else:
#              arrp[i] = 'n'
                
#         if strings[i] == strings[i+1]:
#             s1 = "same"
#             arrs[i] = 's'
#         else:
#             arrs[i] = 'n'
#         i += 1
    
