from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

UDP_IP = "255.255.255.255"
UDP_PORT = 9999

marco = 'Marco!'
polo = 'Polo!'

sock = socket(AF_INET, SOCK_DGRAM) # UDP
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
sock.settimeout(5)

sock.sendto(bytes(marco, "utf-8"), (UDP_IP, UDP_PORT))
print("sent message to " + UDP_IP + ":" + str(UDP_PORT) + ": " + marco)

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode('utf-8')

    print("received message from " + str(addr) + ": ", message)

    if message == 'Polo!':
        print("his IP address is " + str(addr[0]))
        break
