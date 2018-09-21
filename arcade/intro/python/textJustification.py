def format_text( w, L):
    if w and w[0] == " ":
        w = w[1:]
    if w and w[len(w)-1] == " ":
        w = w[:-1]
    space_to_add = L - len(w) 
    arr = w.split(" ")
    if (space_to_add % 2) == 0 and len(arr) > 1:
        if space_to_add > 1:
            n_space_to_add = space_to_add // (len(arr) -1)
            print("@n_space_to_add to add:", n_space_to_add)
            r = ""
            if n_space_to_add == 0 and space_to_add > 0:
                print("space to adad:", space_to_add)
                for a in arr:
                    if space_to_add != 0:
                        r += a + "  "
                        space_to_add -= 1
                    else:
                        r += a + " "
                return r[:-1]
            first_ = True
            for a in arr:
                nn = 0
                if first_:
                    first_ = False
                    if len(arr) > 2  and (len(arr) -1) % 2 != 0:
                        nn =  1
                r += a + str("".join([" " for i in range(0, n_space_to_add+ 1 + nn)]))
            r = r[:-(n_space_to_add+1)]
            print("R:", r)
            return r
    elif (space_to_add % 2) == 0 and len(arr) == 1:
        r = ""
        r += arr[0]+ str("".join([" " for i in range(0, space_to_add)]))
        print("R:",r)
        return r
    elif (space_to_add % 2) != 0 and len(arr) == 1:
        r = ""
        r += arr[0]+ str("".join([" " for i in range(0, space_to_add)]))
        print("R:",r)
        return r
    elif (space_to_add % 2) != 0 and len(arr) > 1:
        r = ""
        if space_to_add == 1:
            r = ""
            i = w.find(' ')
            r = w[:i] + ' ' + w[i:]
            return r

        n_space_to_add = space_to_add // (len(arr) -1)
        print("space_to_add", space_to_add)
        if n_space_to_add == 0 and space_to_add > 0:
            print("space to adad:", space_to_add)
            for a in arr:
                if space_to_add != 0:
                    r += a + "  "
                    space_to_add -= 1
                else:
                    r += a + " "
            return r[:-1]
        first = True
        r = ""
        for a in arr:
            nn = 0
            if first:
                first = False
                if len(arr) % 2 != 0:
                    nn =  1
            new_space = n_space_to_add + 1 + nn
            print("s:", new_space)
            r += a + str("".join([" " for i in range(0, new_space )]))
        r = r[:-(n_space_to_add + 1)]
        return r
    return w
        

def textJustification(words, L):
    new_arr = []
    new_line = ""
    print("Words:",words)
    new_line = ""
    if len(words) == 1:
        new_arr = words
    else:
        for w in words:
            # print("w:", w)
            if new_line and new_line[0] == ' ':
                    new_line = new_line[1:]
            if (len(new_line) + len(w) ) <  L:
                new_line += " " + w
            else:
                if new_line and new_line[0] == ' ':
                    new_line = new_line[1:]
                if new_line:
                    new_arr.append(new_line)
                new_line = ""
                new_line += " " + w
        if new_line and new_line[0] == ' ':
            new_line = new_line[1:]
        new_arr.append(new_line)
    res = []
    if len(new_arr) == 1:
        return [new_arr[0] + str("".join([" " for i in range(0, L - len(new_arr[0]))]))]
    i = 0
    for e in new_arr:
        if i  < len(new_arr)-1:
            res.append(format_text(e,L))
        else:
            res.append(e + str("".join([" " for i in range(0, L - len(e))])))
        i += 1
    return (res)
