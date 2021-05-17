import time
import json
import requests
from plyer import notification

url = 'https://papi.lenovo.com.cn/stock/getStockInfo.jhtm?ss=938&callback=jQueryJSONP_stock_getStockInfo&proInfos=%5B%7BactivityType%3A0%2C+productCode%3A1013205%7D%5D&_=1621241310277'
def get_page():
   a = requests.get(url)
   b = a.text
   c = type(b)
   d = b[32:-2]
   e = json.loads(d)
   f = int(e['salesNumber'])
   g = type(f)
   if f != 0 :
       print("有货了")
       print(f)
       notification.notify(
           title="有货了",
           message="抢！",
           timeout =10)
       time.sleep(2)
   else:
       print("还没有")
       print(time.asctime(time.localtime(time.time())))
       time.sleep(1)

if __name__ == '__main__':
    while 1:
        get_page()
