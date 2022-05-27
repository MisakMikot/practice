import socket
import sys
import threading

s = None  # init socket


def msg_handle():
    global s  # use global variable
    while True:
        try:
            data = s.recv(1024)  # Receive data from the server
            data = data.decode('utf-8')  # Decode data
            print(data)  # Print the data
        except ConnectionResetError:
            print("Server closed connection")
            sys.exit(0)


def main():
    '''
    This is the main function of the client.
    :return:
    '''
    global s  # use global variable
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket
    hostname = input("Enter hostname: ")  # Get hostname
    port = int(input("Enter port: "))  # Get port
    s.connect((hostname, port))  # Connect to the server
    print('Connected to server!')
    name = input("Enter your name: ")  # Register client to the server
    s.send(name.encode('utf-8'))  # Send name to the server
    t = threading.Thread(target=msg_handle)  # Create a thread to handle messages
    t.start()  # Start the thread
    while True:
        msg = input()  # Get message from the user
        try:
            s.send(msg.encode('utf-8'))  # Send message to the server
        except ConnectionResetError:
            print('Connection reset by peer')
            break
        if msg == '/exit':  # If the message is /exit, break the loop
            s.send(msg.encode('utf-8'))
            break
    s.close()  # Close the socket
    sys.exit()  # Exit the program


if __name__ == '__main__':
    main()  # Call main function
