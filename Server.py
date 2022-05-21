import socket
import sys
import os
import platform
import subprocess
host = "127.0.0.1"
port = 8087

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket has been created\n')

def server(sock):
    try:
        sock.bind((host, port))
        print('host Succesfully binded !\n')
        try :    
            sock.listen(1)
            print(f"Server {host} is listening on port {port}\n")
            connection_infos ,(client_host, client_port) = sock.accept()
            print(f'Connection From: {client_host} on Port {client_port}\n')
            connection_infos.sendall(f" Your Connected to a : {platform.uname().system} && version : {platform.uname().version} && User : {os.getlogin( )} \n".encode())
            while True:
                connection_infos.sendall("Type your Commande : \n".encode())
                request = connection_infos.recv(2048)
                connection_infos.sendall(os.system(request.decode()))

        except Exception as e :
            print('failed to listen ! : '+e)
    except Exception as err:
        print ('Binding has failed. Error Code is : ' + str(err[0])+ ' Message : ' + err[1])
        sys.exit()





