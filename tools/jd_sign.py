# Source Generated with Decompyle++
# File: jd_sign.pyc (Python 3.9)

import base64
import requests
import hashlib


def jd_time():
    """
    从京东服务器获取时间戳
    """
    JD_url = "https://api.m.jd.com/api"
    params = {
        "appid": "paimai",
        "functionId": "getPaimaiRealTimeData",
        "body": '{"paimaiId": 3257874327}',
    }
    response = requests.get(JD_url, params, **("params",))
    data = response.json()
    if response.status_code == 200 and data["status"] == 0:
        server_now_time = data["data"]["serverNowTime"]
        return server_now_time


def getSign(params):
    key = [55, 146, 68, 104, 165, 61, 204, 127, 187, 15, 217, 136, 238, 154, 233, 90]
    arg0 = [
        56,
        48,
        51,
        48,
        54,
        102,
        52,
        51,
        55,
        48,
        98,
        51,
        57,
        102,
        100,
        53,
        54,
        51,
        48,
        97,
        100,
        48,
        53,
        50,
        57,
        102,
        55,
        55,
        97,
        100,
        98,
        54,
    ]
    sign = (
        "functionId="
        + params.get("functionId")
        + "&body="
        + params.get("body")
        + "&uuid="
        + params.get("uuid")
        + "&client="
        + params.get("client")
        + "&clientVersion="
        + params.get("clientVersion")
        + "&st="
        + str(params.get("st"))
        + "&sv="
        + str(params.get("sv"))
    )
    arg2 = bytearray(sign, "utf-8")
    ss = [None] * len(arg2)
    for i in range(len(arg2)):
        R0 = arg2[i]
        R2 = key[i & 15]
        R4 = arg0[i & 7]
        R0 = (R2 ^ R0 ^ R4) + R2
        R2 = R2 ^ R0
        R1 = arg0[i & 7]
        R2 = R2 ^ R1
        ss[i] = R2
    m = hashlib.md5()

    def process_list(ss):
        return [i % 256 for i in ss]

    m.update(base64.b64encode(bytes(process_list(ss))))
    return (str(params.get("st")), m.hexdigest(), str(params.get("sv")))


def generateSign():
    params = {
        "st": jd_time(),
        "sv": "120",
        "functionId": "serverConfig",
        "uuid": "f3a6322845f49a67",
        "client": "apple",
        "clientVersion": "12.1.4",
        "body": "{}",
    }
    return getSign(params)


if __name__ == "__main__":
    generateSign()
