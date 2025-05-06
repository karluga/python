import urllib.request, urllib.parse, urllib.error
import ssl

fhand = urllib.request.urlopen('https://publicva.weebly.com/uploads/1/5/2/7/152711807/ziedonis.txt', context=ssl.create_default_context())

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

