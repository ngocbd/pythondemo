import re
import socket
handle=open("regex_sum_201021.txt")
print sum( int(items) for items in re.findall('[0-9]+',handle.read()) )