from socket import socket, AF_INET, SOCK_DGRAM

UDP_IP = "0.0.0.0"
UDP_PORT = 9999

marco = 'Marco!'
polo = 'Polo!'

sock = socket(AF_INET, SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    message = data.decode('utf-8')

    print("received message from " + addr[0] + ":" + str(addr[1]) + ": " + message)

    if message == marco:
        sock.sendto(bytes(polo, 'utf-8'), addr)
        print("replied with: " + polo)
