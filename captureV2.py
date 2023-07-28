import pyautogui, time
import requests
import os

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
    
    #####    
    fileTest = "screenshot-"+ str(i-1) +".png" # 因為照片在傳出去的時候會鎖死刪不掉，所以要刪前一個檔案
    try: # 防止找不到檔案導致程式停止
        os.remove(fileTest) # 刪除截圖的圖片檔案
    except OSError as e:
        print(e) # 印出錯誤訊息
    
    time.sleep(5) #看你要幾秒鐘偷窺一次
    i = i + 1