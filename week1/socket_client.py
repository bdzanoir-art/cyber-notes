import socket

HOST, PORT = "127.0.0.1", 8000
PATH = "/admin/login/"  # change this to test other routes

request = (
    f"GET {PATH} HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    "Connection: close\r\n"
    "\r\n"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(request.encode())
    response = b""
    while chunk := s.recv(4096):
        response += chunk

print(response.decode(errors="replace"))
