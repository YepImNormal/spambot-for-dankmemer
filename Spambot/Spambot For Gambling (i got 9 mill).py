import pyautogui
import webbrowser
import time
import keyboard

message1 = input("Text to be spammed =>")
message2 = input("Text to be spammed =>")


choice = 1


if choice == 1:
    repeats = 1000
    delay = 5000
	
    print("Open up your messaging app, please")
    isLoaded = input("Press Enter when the app is loaded up.")

    print("There is a 10 second cooldown for you to switch to the text input of the messaging app")

    time.sleep(10)

    for i in range(0, repeats):
        if message1 != "":
            pyautogui.typewrite(message1)
            pyautogui.press("enter")
            time.sleep(2)
        if message2 != "":   
            pyautogui.typewrite(message2)
            pyautogui.press("enter")
            time.sleep(5)
        else:
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")

        time.sleep(delay/1000)

    final = input("Worked like a charm. Have a good day! (press enter to close this window)")


    print("This mode of spammer runs forever. Remember, to stop spamming, press Ctrl+Shift+W and the program will stop!")
    print("Open up your messaging app, please")
    isLoaded = input("Press Enter when the app is loaded up.")

    print("There is a 10 second cooldown for you to switch to the text input of the messaging app")

    time.sleep(10)

    keyboard.add_hotkey('ctrl+shift+w', stop_spammer)

