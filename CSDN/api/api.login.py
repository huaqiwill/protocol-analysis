import requests
import json


def do_login():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
    }
    data = {
        "agreedPrivacyPolicy": 0,
        "loginType": "1",
        "pwdOrVerifyCode": "hanying1234.pcf",
        "uaToken": "",
        "userIdentification": "HuaQi666",
        "webUmidToken": "",
    }
    json_data = json.dumps(data)
    response = requests.post(
        "https://passport.csdn.net/v1/register/pc/login/doLogin",
        data=json_data,
        headers=headers,
    )
    # print(response.content.decode("utf-8"))
    print(response.headers["Set-Cookie"])


if __name__ == "__main__":
    do_login()
