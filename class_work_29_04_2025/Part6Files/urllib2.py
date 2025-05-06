import urllib.request, urllib.parse, urllib.error
import ssl

fhand = urllib.request.urlopen('http://publicva.atwebpages.com/pyt/page01.htm', context=ssl.create_default_context())
for line in fhand:
    print(line.decode().strip())
