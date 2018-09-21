def reverseParentheses(s):
    if '(' not in s:
        return s
    else:
        i_l = s.rfind('(')
        tmp_s = s[i_l:]
        i_r = tmp_s.find(')')
        new_s = tmp_s[:i_r+1]
        new_s = new_s[1:]
        new_s = new_s[:-1]
        new_s = new_s[::-1]
        new_change_string = s[:i_l] + new_s + s[i_l+i_r+1:]
        return reverseParentheses(new_change_string)

