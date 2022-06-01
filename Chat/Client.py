import socket
import sys
import threading
import json

s = None  # init socket



def msg_handle():
    global s  # use global variable
    while True:
        try:
            data = s.recv(1024)  # Receive data from the server
            data = data.decode('utf-8')  # Decode data
            data = eval(data)  # Convert data to json
            if data['type'] == 'message':  # If the data is a message
                print(data['from']+' : '+data['data'])  # Print the messages
            elif data['type'] == 'userlist':  # If the data is a userlist
                print('Userlist:')
                for user in data['data']:  # Print each user
                    print(user)
            elif data['type'] == 'error':  # If the data is an error
                print(data['data'])  # Print the error
            elif data['type'] == 'svrcmd':  # If the data is a server command
                if data['data'] == 'exit':  # If the command is exit
                    s.close()  # Close the socket
                    sys.exit()  # Exit the program
                elif data['data'] == 'reconnect':  # If the command is reconnect
                    s.close()  # Close the socket
                    main()  # Restart the program
            else:
                s.send('{"type": "error", "data": "Unknown command"}'.encode('utf-8'))  # Send an error
        except ConnectionResetError:
            print("Server closed connection")
            sys.exit(0)
        except SyntaxError:
            print('ERR_EMPTY_RESPONSE')


def main():
    '''
    This is the main function of the client.
    :return:
    '''
    global s  # use global variable
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket
    hostname = input("Enter hostname: ")  # Get hostname
    port = input("Enter port: (15587)")  # Get port
    if port == '':
        port = int(15587)  # Set default port
    else:
        port = int(port)  # Set port
    s.connect((hostname, port))  # Connect to the server
    print('Connected to server!')
    name = input("Enter your name (Anonymous): ")  # Register client to the server
    temp = '{"type": "register", "data": "' + name + '"}'  # Create register message
    s.send(temp.encode('utf-8'))  # Send register command to the server
    t = threading.Thread(target=msg_handle)  # Create a thread to handle messages
    t.start()  # Start the thread
    while True:
        msg = input("->")  # Get message from the user
        if msg.startswith('/'):  # If the message starts with a slash
            if msg == '/exit':  # If the message is exit
                s.send('{"type": "svrcmd", "data": "exit"})'.encode('utf-8'))  # Send exit command to the server
                break  # Break the loop
        try:
            temp = '{"type": "message", "data": "' + msg + '", "from": "'+name+'"}'  # Create message
            s.send(temp.encode('utf-8'))  # Send message to the server
        except ConnectionResetError:
            print('Connection reset by peer')
            break
    s.close()  # Close the socket
    sys.exit()  # Exit the program


if __name__ == '__main__':
    main()  # Call main function
