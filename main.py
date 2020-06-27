import pyperclip
import keyboard
from time import sleep

old_clipboard = ""
new_clipboard = ""

while True:
    pyperclip.waitFornewPaste()
    
    if keyboard.read_key() == "esc":
        break
    
    old_clipboard = new_clipboard
    new_clipboard = pyperclip.paste()
    
    pyperclip.copy(old_clipboard)
    sleep(5)
    pyperclip.copy(new_clipboard)
