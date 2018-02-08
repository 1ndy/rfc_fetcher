import pydoc
import urllib.request
import sys

if len(sys.argv) != 2:
	print("Program requires exactly one rfc number")
	sys.exit()

rfc_num = sys.argv[1]

url = "https://www.rfc-editor.org/rfc/rfc" + rfc_num + ".txt"

request = urllib.request.Request(url)
try:
	response = urllib.request.urlopen(request)
except:
	print("Error: RFC %s does not exist" % rfc_num)
	sys.exit()
rfc = response.read().decode('utf-8')
pydoc.pager(rfc)

