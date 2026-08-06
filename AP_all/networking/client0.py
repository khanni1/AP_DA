import socket as so

host = 'localhost'
port = 6000

s = so.socket()

s.connect((host,port))

msg = s.recv(1024)

# extra better repeat as long as message string is not empty

while msg:
    print(msg.decode())

msg = s.recv(1024)

s.close()
