import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with client_socket:
    client_socket.connect(('localhost', 10002))
    message = '你的姓名 学号'  # 请替换为实际的姓名和学号
    client_socket.sendall(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f'收到回复: {response}')
    client_socket.close()