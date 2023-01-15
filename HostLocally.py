import http.server
import socketserver
import socket

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(socketserver.socket.gethostbyname(socket.getfqdn()))
    print("serving at port", PORT)
    httpd.serve_forever()
