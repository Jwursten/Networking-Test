import socket

def start_client():
    host = "127.0.0.1"
    port = 5555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    player_number = client_socket.recv(1024).decode()
    print(player_number)

    while True:
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
        client_socket.send(choice.encode())
        result = client_socket.recv(1024).decode()
        print(result)

if __name__ == "__main__":
    start_client()
