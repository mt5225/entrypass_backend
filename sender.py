import socket
import sys

def read_file(file_name):
    """read the message file
    """
    f = open(path,"r")
    file_content = []
    for line in f:
        file_content.append(line)
    return ''.join(file_content)

def send_message(message):
    """ send message to server
    """
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #clientsocket.connect(('localhost', 9005))
    clientsocket.connect(('uinnova.com', 9005))
    clientsocket.send(message)


if __name__ == '__main__':
    path = './msg/' + sys.argv[1] + '.xml'
    send_message(read_file(path))
