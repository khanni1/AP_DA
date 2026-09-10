import socket as so

host  = '0.0.0.0'
port = 6000

s = so.socket(so.AF_INET,so.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
c,addr = s.accept()
print("Connection from:",str(addr))

c.send(b"Hello client ")
msg = "Bye!"
c.send(msg.encode())

c.close()