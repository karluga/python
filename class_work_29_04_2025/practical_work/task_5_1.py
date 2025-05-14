import socket 

try:
    webPage = input("Input webpage address (e.g., example.com): ").strip()
    path = "/"

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((webPage, 80))

    cmd = f"GET {path} HTTP/1.0\r\nHost: {webPage}\r\n\r\n".encode()
    mysock.send(cmd)

    count = 0
    printed_chars = 0
    limit = 1700

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break

        decoded = data.decode(errors = 'replace')
        chars_left = limit - printed_chars

        count += len(decoded)

        if printed_chars < limit:
            to_output = decoded[:chars_left]
            print(to_output, end = '')
            printed_chars += len(to_output)


    print("\n\nTotal number of characters received:", count)
    print("\n\nTotal number of characters printed:", printed_chars)

except Exception as e:
    print("Error:", e)

mysock.close()