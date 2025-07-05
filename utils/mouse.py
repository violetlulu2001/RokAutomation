from pynput import *

def get_coord(x, y):
    print(x, y)


with mouse.Listener(on_move=get_coord) as listen:
        listen.join()
