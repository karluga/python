import urllib.request
import ssl

fhand = urllib.request.urlopen('https://publicva.weebly.com/uploads/1/5/2/7/152711807/ziedonis.txt', context=ssl.create_default_context())
for line in fhand:
    print(line.decode().strip())
    # print(line, "Type:", type(line))