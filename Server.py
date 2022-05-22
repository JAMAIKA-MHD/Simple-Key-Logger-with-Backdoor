import numbers
import socket
import os
import platform
from unicodedata import numeric


def C_server(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket has been created\n')# to be removed
    try:
        sock.bind((ip, port))
        print('host Succesfully binded !\n')# to be removed
    except Exception as err:
        print ('Binding has failed. Error Code is : ' ,err)# to be removed
        exit()

    return sock

def conn_hundler(sock):
    try :    
        sock.listen(1)
        connection_infos ,(client_host, client_port) = sock.accept()
        print(f'Connection From: {client_host} on Port {client_port}\n')# to be removed
        connection_infos.sendall(f" Your Connected to a : {platform.uname().system} && version : {platform.uname().version} && User : {os.getlogin( )} \n".encode())

    except Exception as e :
        print('failed to listen ! : '+e)# to be removed

    return connection_infos

def Sender(remote_host,data):
    try : 
        remote_host.sendall(data.encode())
        return True
    except Exception as e : 
        print(' Error While Sending : %s',e)# to be removed


print(Sender(conn_hundler(C_server('127.0.0.1',8088)),"hello world"))