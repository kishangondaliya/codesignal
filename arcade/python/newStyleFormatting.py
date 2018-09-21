import re
# from string import Template

# def newStyleFormatting(s):
#     s =  s.replace('%','$')
#     t = Template(s)
#     s = t.substitute({'d':'{}', "s":'{}', 'a':'{}', 'f':'{}','b':'{}', 'c':'{}', 'o':'{}','x':'{}', 'X':'{}', 'n':'{}','e':'{}', 'F':'{}', 'g':'{}', 'G':'{}',})
#     return s.replace('$','%')
    
def newStyleFormatting(s):
    return "%".join([re.sub("%([bcdeEfFgGnosxX])","{}",S) for S in s.split("%%")])
