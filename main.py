import datetime
import zoneinfo

# 設定時區為台北
taipei_tz = zoneinfo.ZoneInfo("Asia/Taipei")

# 獲取當前台北時間
now_in_taipei = datetime.datetime.now(taipei_tz)

# 格式化輸出
formatted_time = now_in_taipei.strftime("%Y-%m-%d %H:%M:%S")

print(f"Hello from GitHub Actions!")
print(f"The current time in Taipei is: {formatted_time}")

# 假設您的腳本需要用到套件，可以取消下面這行的註解
# import requests
# print("Requests library version:", requests.__version__)
