from  pyperclip import copy, paste, waitForNewPaste
import keyboard, multiprocessing, json

def duplicate_clipboard(switch_key, clear):
    while True:
        old = waitForNewPaste()
        new = waitForNewPaste()
        
        copy(old)

        keyboard.wait(switch_key)
        copy(new)
        print("Clipboard switched!")

        if clear == True:
            old = ""
            new = ""
            
            keyboard.wait(switch_key)
            copy("")
            print("Clipboard cleared!")

def check_end():
    keyboard.wait("esc")
    copy("")

if __name__ == "__main__":
    with open("settings.json") as r:
        settings = json.load(r)
    switch_key = settings["key"]
    clear = settings["clear"]
    assert type(clear) == bool, "'clear' from settings.json is not boolean"
    assert type(switch_key) == str, "'key' from settings.json is not string"
    
    p1 = multiprocessing.Process(target=duplicate_clipboard, args=(switch_key, clear))
    p1.start()
    p2 = multiprocessing.Process(target=check_end)
    p2.start()

    p2.join()
    p1.close()
    raise KeyboardInterrupt("Program killed. Clipboard cleared")
