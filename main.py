from  pyperclip import copy, paste, waitForNewPaste
import keyboard, multiprocessing

switch_key = "right alt"

def duplicate_clipboard():
    while True:
        old = waitForNewPaste()
        new = waitForNewPaste()
        
        copy(old)

        keyboard.wait(switch_key)
        copy(new)
        print("Clipboard switched!")

        old = ""
        new = ""
        
        keyboard.wait(switch_key)
        copy("")
        print("Clipboard cleared!")

def check_end():
    keyboard.wait("esc")
    copy("")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=duplicate_clipboard)
    p2 = multiprocessing.Process(target=check_end)

    p1.start()
    p2.start()

    p2.join()
    raise Exception("Program killed. Clipboard cleared")
