import socket
import ssl
import pprint

browser = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36\r\n" + "Accept-Language: en-GB,en;q=0.5\r\n\r\n"  
package = "GET /uploads/1/5/2/7/152711807/ziedonis.txt HTTP/1.1\r\n" + "Host: publicva.weebly.com\r\n" + browser

mycontext_ssl = ssl.create_default_context()
mysock_ssl = mycontext_ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),server_hostname="publicva.weebly.com")
mysock_ssl.connect(("publicva.weebly.com", 443))

print("CERTIFICATE:")
pprint.pprint(mysock_ssl.getpeercert())
print('\n')

# print("VERSION:\n", mysock_ssl.version(), "\n\n")

# mysock_ssl.send(package.encode())
# while True:
#     data = mysock_ssl.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock_ssl.close()
