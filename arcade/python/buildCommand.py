import json
from collections import OrderedDict
import numbers
import decimal



def myprint(d):
  for k, v in d.items():
      if isinstance(v, str):
        d[k] =  ""
      elif isinstance(v, list):
        d[k] = []
      elif isinstance(v, int):
        d[k] = 0
      elif isinstance(v, numbers.Number):
        d[k] = 0      
      elif isinstance(v, decimal.Decimal):
        d[k] = 0
      elif isinstance(v, dict):
        myprint(v)
      else:
        print("new type:", type(v))
      print("k:{}, v:{}".format(k,v))
  return d


def buildCommand(jsonFile):
    j = json.loads(jsonFile, object_pairs_hook = OrderedDict)
    j = myprint(j)
    return json.dumps(j)
