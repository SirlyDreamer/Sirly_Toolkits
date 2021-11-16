import requests
import time

headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",}
def login():
    username=""
    passwd=""
    url = 'http://10.220.250.50/0.htm'
    payload = {"DDDDD":"%s"%username,
            "upass":"%s"%passwd,
            "suffix":"123456",
            "0MKKey":"123"}
    try:
        requests.post(url,data=payload,headers=headers)
        return 1
    except requests.exceptions.RequestException as errinfo:
        print(errinfo)
        return 0

def testNet(url):
    try:
        r = requests.get(url,headers=headers,timeout=(3.05,12.05))
        return r.status_code == 200
    except requests.exceptions.RequestException as errinfo:
        print(errinfo)
        return 0

def main():
    while True:
        if(testNet("https://www.bilibili.com")):
            SleepTime = 600
            print (time.strftime("[%Y-%m-%d %H:%M:%S] Network Connect Succeed!", time.localtime()))  
        else:
            print (time.strftime("[%Y-%m-%d %H:%M:%S] Network Connect Failed, trying to login...", time.localtime()))
            if(testNet("http://10.220.250.50")):
                if(login()):
                    SleepTime = 10
                    print (time.strftime("[%Y-%m-%d %H:%M:%S] Login Request Sent", time.localtime()))
                else:
                    SleepTime = 30
                    print (time.strftime("[%Y-%m-%d %H:%M:%S] Login Failed, will try 30s later...", time.localtime()))
            else:
                SleepTime = 60
                print (time.strftime("[%Y-%m-%d %H:%M:%S] Auth Server Connect Failed, waiting for 60s...", time.localtime()))
        time.sleep(SleepTime)

main()
