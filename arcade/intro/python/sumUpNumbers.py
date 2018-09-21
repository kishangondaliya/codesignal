
def check_num(e):
  try:
    return int(e)
  except ValueError:
    return 0


def sumUpNumbers(inputString):
  arr = []
  for e in re.findall(r"[^\W\d_]+|\d+",inputString):
    arr.append(check_num(e))
  return sum(arr)
