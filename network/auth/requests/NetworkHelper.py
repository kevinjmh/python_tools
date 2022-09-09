import time

import requests
from requests_toolbelt import SSLAdapter


if __name__ == '__main__':
    f = open("network.ticket.ini", "r")
    url = f.readline().strip()
    username = f.readline().strip()
    passwd = f.readline().strip()
    auth_url = f.readline().strip()
    auth_tag = f.readline().strip()
    auth_pwd = f.readline().strip()
    f.close()

    headers = {
        "Proxy-Connection": "keep-alive",
        "Pragma": "no-cache",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4",
        "Accept-Charset": "utf-8",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest"
    }
    body_value = {"auth_tag": auth_tag,
                  "opr": "pwdLogin",
                  "pwd": auth_pwd,
                  "rememberPwd": "0",
                  "userName": username}

    session = requests.session()
    adapter = SSLAdapter('TLSv1')
    session.mount('https://', adapter)
    req = session.post(auth_url, data=body_value, headers=headers, verify=False)
    res = req.text
    print(res)

    time.sleep(2)
