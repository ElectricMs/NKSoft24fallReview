import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = 'hello'  # 请替换为实际的姓名和学号

with client_socket:
    sent = client_socket.sendto(message.encode('utf-8'), ('localhost', 10001))
    data, addr = client_socket.recvfrom(1024)
    response = data.decode('utf-8')
    print(f'收到回复: {response}')
    client_socket.close()