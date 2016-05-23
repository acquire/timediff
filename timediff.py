import sys
from datetime import datetime

a = datetime.strptime(sys.argv[1],"%I:%M%p")
b = datetime.strptime(sys.argv[2],"%I:%M%p")

print(a-b)