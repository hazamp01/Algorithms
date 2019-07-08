import urllib
import json

data = urllib.urlopen("http://api.fixer.io/latest?base=GBP").read()
data = json.loads(data)

print(data)