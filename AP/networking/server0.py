import socket as so

host = 'localhost'
port = 6000

s = so.socket()

s.bind((host,port))

s.listen(1)

c,addr = s.accept()

# after here runtime then waiting for client to accept

print(str(addr))

c.send(b"Hello client ")

msg = "BYE"

c.send(msg.encode())

c.close()

# imp dont close socket close connection only