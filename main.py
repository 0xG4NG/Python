import re
import socket
import PyQt6

pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
log = open("access.log", "r")
text = log.read()
ip_address = re.findall(pattern, text)

for i in ip_address:
    print(i)

