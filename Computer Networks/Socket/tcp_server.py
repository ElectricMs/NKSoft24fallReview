import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 10002))
server_socket.listen(1)
print('服务器已启动，等待连接...')

while True:
    # 当有客户端连接时，accept()方法会返回一个新的套接字对象client_socket和客户端的地址 addr
    client_socket, addr = server_socket.accept()
    with client_socket:
        print(f'连接来自 {addr}')
        data = client_socket.recv(1024).decode('utf-8')
        client_socket.sendall(f'Welcome {addr[0]}'.encode('utf-8'))
        client_socket.close()