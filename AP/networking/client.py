import socket as so

host = '127.0.0.1'
port = 6000

s = so.socket(so.AF_INET,so.SOCK_STREAM)

s.connect((host,port))

msg = s.recv(1024)
# Extra : repeat as long as message strings are not empty
while msg:
    print('Received : ', msg.decode())
    msg = s.recv(1024)
    

s.close()