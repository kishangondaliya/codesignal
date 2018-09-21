
def is_vowel(s):
  if s in ['a','e','u','i','o'] or s in ['A', 'E', 'U', 'I', 'O']:
    return True
  return False

def reverseVowelsOfString(s):
  s_list = list(s)
  s_len =  len(s_list) -1
  i = 0
  j = s_len
  while i < s_len and j != i:
    if is_vowel(s_list[i]):
      while j > 0 and j > i:
        if is_vowel(s[j]):
          tmp = s_list[i]
          s_list[i] = s_list[j]
          s_list[j] = tmp
          j -= 1
          break
        j -= 1
    i += 1
  return ''.join(s_list)
