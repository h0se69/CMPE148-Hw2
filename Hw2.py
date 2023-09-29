# import socket module
from socket import *
import sys  # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket

#Fill in start
server_name = "SJSU Campus"
serer_port = 6969

serverSocket.bind(("", serer_port))
serverSocket.listen(1)

#Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    
    # Fill in start 
    connectionSocket, addr = serverSocket.accept()

    #Fill in end
    try:
        # Fill in start 
        message = connectionSocket.recv(1024)
        #Fill in end

        filename = message.split()[1]

        f = open(filename[1:])

        # Fill in start 
        outputdata =  f.read()
        f.close()
        #Fill in end


        #Send one HTTP header line into socket
        #Fill in start
        http_header ="HTTP/1.1 200 OK\r\n\r\n".encode()
        connectionSocket.send(http_header)
        #Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    
    except IOError as io_error:
        #Send response message for file not found
        #Fill in start
        error_msg = "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        connectionSocket.send(error_msg)
        #Fill in end

        #Close client socket
        #Fill in start
        # print("closing socket now...")
        connectionSocket.close()
        #Fill in end

# Note to Prof: This part of the code was outside the True block, is it supposed to be like this? It will never be reached
serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
