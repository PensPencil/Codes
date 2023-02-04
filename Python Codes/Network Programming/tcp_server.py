from audioop import add
import socket

s = socket.socket()
host = socket.gethostname()
port = 9999

s.bind((host,port))

print("Waiting for Connection")
s.listen(5)

while(True):
    conn,addr = s.accept()
    print("Got connection from ",addr)
    conn.send("Server saying Hi")
    conn.close()