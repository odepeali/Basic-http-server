import socket

HOST = '127.0.0.1'
PORT = 9091

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Serving HTTP on {HOST}:{PORT}...")

while True:
    client_conn, client_addr = server_socket.accept()
    request = client_conn.recv(1024).decode('utf-8')
    print("Received request:\n", request)

    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        "Connection: close\r\n"
        "\r\n"
        "<html><body><h1>Hello, World!</h1></body></html>"
    )

    