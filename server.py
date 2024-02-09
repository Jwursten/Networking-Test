import socket

def play_game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (
        (player1_choice == "rock" and player2_choice == "scissors")
        or (player1_choice == "paper" and player2_choice == "rock")
        or (player1_choice == "scissors" and player2_choice == "paper")
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def start_server():
    host = "127.0.0.1"
    port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    player1, addr1 = server_socket.accept()
    print(f"Player 1 connected from {addr1}")

    player2, addr2 = server_socket.accept()
    print(f"Player 2 connected from {addr2}")

    player1.send("You are Player 1".encode())
    player2.send("You are Player 2".encode())

    while True:
        player1_choice = player1.recv(1024).decode().lower()
        player2_choice = player2.recv(1024).decode().lower()

        result = play_game(player1_choice, player2_choice)
        player1.send(result.encode())
        player2.send(result.encode())

if __name__ == "__main__":
    start_server()
