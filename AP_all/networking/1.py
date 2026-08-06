import socket as so
# s = so.so(address_family, type)

s = so.socket(so.AF_INET, so.SOCK_STREAM) # IPv4 TCP/IP
print(s)

a = so.socket(so.AF_INET6, so.SOCK_DGRAM) # IPv6 UDP
print(a)
addr1 = so.gethostbyname("www.google.com")
print(addr1)

# name = so.gethostbyaddr(addr1) error for host not found

name = so.gethostbyaddr("0.0.0.0")
print(name)

name = so.gethostbyaddr("8.8.8.8")
print(name)

