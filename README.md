# Networking-Test
A python based LAN game

# Overview

This was created to learn more about how to implement networking into coding. 

The networking program I provided is a simple rock-paper-scissors game implemented using Python's socket module. It consists of two scripts: server.py for the server and client.py for the clients. Server,py establishes a server that listens for connections on a specific IP address and port. It waits for two clients to connect, assigns them player numbers, and then facilitates the rock-paper-scissors game between them. The server communicates with the clients to exchange information about player numbers, choices, and game results. Client.py represents a client that connects to the server. Each client receives a player number (Player 1 or Player 2) upon connection. The client prompts the user to input their choice (rock, paper, or scissors) and sends this choice to the server.

I wanted to learn about networking and how it is implemented in python.

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/N1i6WIIAAC8)

# Network Communication

The server manages the game logic, listens for connections, assigns player numbers, and facilitates communication between the two clients. The clients connect to the server, receive player numbers, interact with users to input choices and receive and display the game results from the server. This client-server architecture allows for central control of the game, making it easy to manage the flow of information and decisions in a coordinated manner.

The provided program uses TCP for communication between the server and clients. The port number used in this implementation is 5555. Both the server and clients are configured to use this port for communication.

Messages between the client and server are encoded as strings. The communication is based on a simple protocol where messages are exchanged in a human-readable format. The format of the messages involves sending strings that convey specific information.

# Development Environment

I used python and VS Code.

I used the socket library of Python

# Useful Websites

* [Python Documentation]((https://docs.python.org/3.6/library/socket.html))
* [Data Camp]((https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python))

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Allow error testing
* Allow input to connect
* more games?
