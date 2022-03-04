import requests
import time

headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",}
            
def login():
    username=""
    passwd=""
    url = 'http://10.220.250.50/1.html'
    payload = {"DDDDD":"%s"%username,
            "upass":"%s"%passwd,
            "suffix":"123456",
            "0MKKey":"123"}
    for i in range(3):
        try:
            r = requests.post(url,data=payload,headers=headers)
            if r.status_code == 200:
                return True
        except requests.exceptions.RequestException as errinfo:
            print(errinfo)
        time.sleep(1)
    return False

def testNet(url):
    for i in range(3):
        try:
            r = requests.get(url,headers=headers,timeout=(3.05,12.05))
            if r.status_code == 200:
                return True
        except requests.exceptions.RequestException as errinfo:
            print(errinfo)
        time.sleep(1)
    return False

def main():
    while True:
        if(testNet("https://www.baidu.com")):
            SleepTime = 600
            print (time.strftime("[%Y-%m-%d %H:%M:%S] Network Connect Succeed!", time.localtime()))  
        else:
            print (time.strftime("[%Y-%m-%d %H:%M:%S] Network Connect Failed, trying to login...", time.localtime()))
            while True:
                if(testNet("http://10.220.250.50")):
                    if(login()):
                        SleepTime = 10
                        print (time.strftime("[%Y-%m-%d %H:%M:%S] Login Request Sent", time.localtime()))
                        break
                    else:
                        SleepTime = 30
                        print (time.strftime("[%Y-%m-%d %H:%M:%S] Login Failed, will try 30s later...", time.localtime()))
                else:
                    SleepTime = 60
                    print (time.strftime("[%Y-%m-%d %H:%M:%S] Auth Server Connect Failed, waiting for 60s...", time.localtime()))
                time.sleep(SleepTime)
        time.sleep(SleepTime)

main()