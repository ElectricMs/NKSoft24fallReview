import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 10001))

while True:
    data, addr = server_socket.recvfrom(1024)  # 接收数据和客户端地址
    message = data.decode('utf-8')
    print(f'收到消息: {message} 来自 {addr}')
    
    if message:
        response = f'Welcome {addr[0]}'
        print(f'发送回复: {response}')
        server_socket.sendto(response.encode('utf-8'), addr)