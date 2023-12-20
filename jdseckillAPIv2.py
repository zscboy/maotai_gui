# Source Generated with Decompyle++
# File: jdseckillAPIv2.pyc (Python 3.9)

import json
import logging
import warnings
import requests
import re
from urllib import parse
import time

# from tools.jd_sign import getSign
# from wxpusher import WxPusher
from tools import utils
from config_function import read_config

warnings.filterwarnings("ignore")
(
    ZCSUPER_cookie,
    zcsuper_key,
    ZCSUPER_uuid,
    ZCSUPER_eid,
    ZCSUPER_uts,
    ZCSUPER_area,
    zcsuper_sku,
    zcsuper_user_killTime,
) = read_config()
GET_PROXY_RESP = requests.get("https://docs.zcsuper.cn/python/proyx_config.json")
PROXY_CONFIG = GET_PROXY_RESP.json()
proxyAddr = PROXY_CONFIG["param1"]
authKey = PROXY_CONFIG["param2"]
password = PROXY_CONFIG["param3"]

proxyUrl = f"http://{authKey}:{password}@{proxyAddr}"
# proxies = {proxyUrl: proxyUrl}


# 检查代理服务状态proxyUrl = f"http://{authKey}:{password}@{proxyAddr}"
proxies = {"http": proxyUrl, "https": proxyUrl}
try:
    response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
    if response.status_code == 200:
        print("代理服务状态：正常")
        logging.info("代理服务状态：正常")
    else:
        print("代理服务状态：异常")
        logging.info("代理服务状态：异常")
except requests.exceptions.RequestException as e:
    logging.info("代理服务状态：" + str(e))


def getUrlParams(url):
    res = parse.parse_qsl(url)
    return res


def get_cookie_string(cookie):
    cookie_string = ""
    for cookie_key in cookie.keys():
        cookie_string += "%s=%s;" % (cookie_key, cookie[cookie_key])
    return cookie_string


def get_jd_time():
    JD_url = "https://api.m.jd.com/api"
    params = {
        "appid": "paimai",
        "functionId": "getPaimaiRealTimeData",
        "body": '{"paimaiId": 3257874327}',
    }
    response = requests.get(JD_url, params=params)
    data = response.json()
    if response.status_code == 200 and data["status"] == 0:
        server_now_time = data["data"]["serverNowTime"]
        return server_now_time
    else:
        print("京东服务器获取时间失败！")
        print(response.json())
        return None


def get_sk(data):
    def get_sk_val(val):
        return val

    data_val = data["data"][0:6]
    n, o, p, q, r, s = data_val
    sk_val = ""
    if n == "cca":
        sk_val = p[14:19].lower() + o[5:15].upper()
    elif n == "ab":
        sk_val = r[10:18].lower() + s[6:13].upper()
    elif n == "ch":
        sk_val = q.upper() + r[6:10].upper()
    elif n == "cbc":
        sk_val = q[3:13].upper() + p[2:13].lower()
    elif n == "by":
        sk_val = o[5:8] + re.sub("a", "c", p, flags=re.IGNORECASE)
    elif n == "xa":
        sk_val = o[1:16] + s[4:10]
    elif n == "cza":
        sk_val = s[5:11].lower() + r[10:19].lower()
    elif n == "cb":
        sk_val = s[5:14].upper() + p[2:13].lower()
    elif n == "b":
        sk_val = o[5:8] + p.upper() + p[2:13].lower()
    return sk_val


class JDSecKillAPI:
    def __init__(self, sku, ck):
        self.skuId = sku
        self.s = requests.session()
        self.sku = sku
        self.ck = ck
        self.aid = ""
        self.eid = ZCSUPER_eid
        self.uuid = ZCSUPER_uuid
        self.uts = ZCSUPER_uts
        self.wifiBssid = ""
        self.ua = "AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
        self.proxies = None

    def appoint_sku(self, ck):
        ua = "JD4iPhone/168898%20(iPhone;%20iOS;%20Scale/2.00);jdmall;iphone;version/12.1.4;build/168898;network/wifi;screen/828x1792;os/16.6"
        s = self.s
        headers = {
            "user-agent": ua,
            "content-type": "application/x-www-form-urlencoded",
            "cookie": self.ck,
            "jdc-backup": self.ck,
        }
        ts = int(time.time() * 1000) - 71700
        uuid = utils.get_ep(ts, s.cookies["sid"])
        body = {
            "skuId": self.sku,
            "num": num,
            "addressId": address_id,
            "yuShou": True,
            "isModifyAddress": False,
            "name": address_info["name"],
            "provinceId": address_info["provinceId"],
            "provinceName": address_info["provinceName"],
            "cityId": address_info["cityId"],
            "cityName": address_info["cityName"],
            "countyId": address_info["countyId"],
            "countyName": address_info["countyName"],
            "townId": address_info["townId"],
            "townName": address_info["townName"],
            "addressDetail": address_info["addressDetail"],
            "mobile": address_info["mobile"],
            "mobileKey": address_info["mobileKey"],
            "email": "",
        }
        data = {
            "url": "https://marathon.jd.com/seckillnew/orderService/init.action",
            "data": body,
            "allow_redirects": False,
            "verify": False,
            "headers": headers,
        }

        try:
            response = s.post(
                "https://marathon.jd.com/seckillnew/orderService/init.action", body
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def get_token_key(self):
        ua = "JD4iPhone/168898%20(iPhone;%20iOS;%20Scale/2.00);jdmall;iphone;version/12.1.4;build/168898;network/wifi;screen/828x1792;os/16.6"
        s = self.s
        headers = {ua}
        ts = int(time.time() * 1000) - 71700
        uuid = get_ep(ts, s.cookies["sid"])
        data = {
            "url": "https://api.m.jd.com/client.action",
            "data": {
                "functionId": "genToken",
                "clientVersion": "ios_3.0.0",
                "uuid": uuid,
                "client": "apple",
            },
        }

        try:
            response = s.post("https://api.m.jd.com/client.action", data)
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def get_appjmp(self, ua, s, get_sk):
        headers = {ua}
        sk = get_sk(s.cookies["sid"], headers)
        params = {
            "to": "https://divide.jd.com/user_routing?skuId=" + self.skuId,
            "tokenKey": sk,
        }
        try:
            response = s.get(
                "https://divide.jd.com/user_routing",
                params=params,
                allow_redirects=False,
                verify=False,
                headers=headers,
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def get_divide(self, ua, s, get_sk):
        headers = {ua}
        sk = get_sk(s.cookies["sid"], headers)
        params = {
            "to": "https://marathon.jd.com/seckillnew/orderService/init.action",
            "tokenKey": sk,
        }
        try:
            response = s.get(
                "https://marathon.jd.com/seckillnew/dynamic/split",
                params=params,
                allow_redirects=False,
                verify=False,
                headers=headers,
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def get_captcha(self, ua, s, get_sk):
        headers = {ua}
        sk = get_sk(s.cookies["sid"], headers)
        params = {
            "to": "https://marathon.jd.com/seckillnew/orderService/pc/popCaptcha.action?tokenKey="
            + sk
        }
        try:
            response = s.get(
                "https://marathon.jd.com/seckillnew/dynamic/split",
                params=params,
                allow_redirects=False,
                verify=False,
                headers=headers,
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def visit_seckill(self, ua, s, get_sk):
        headers = {ua}
        sk = get_sk(s.cookies["sid"], headers)
        params = {
            "to": "https://marathon.jd.com/seckillnew/orderService/pc/popCaptcha.action?tokenKey="
            + sk
        }
        try:
            response = s.get(
                "https://marathon.jd.com/seckillnew/orderService/pc/popCaptcha.action",
                params=params,
                allow_redirects=False,
                verify=False,
                headers=headers,
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def init_action(self, ua, skuId, s, post, json):
        headers = {ua, "keep-alive", "Connection"}
        init_action_url = "https://marathon.jd.com/seckillnew/orderService/init.action"
        data = {
            "skuId": skuId,
            "num": 1,
            "id": 8190309,
            "provinceId": 1,
            "provinceName": "北京市",
            "cityId": 72,
            "cityName": "北京市",
            "countyId": 2799,
            "countyName": "朝阳区",
            "townId": 4117,
            "townName": "将台街道办事处",
            "addressDetail": "亚运村中路36号第一创业大厦北区B座1层星美影城",
            "mobile": "136****788",
            "mobileKey": "Fe3nIi/Tw7nIsYXbM0nd23Xtbnn4PQc9bxC0Eq",
        }

        try:
            response = s.post(
                "https://marathon.jd.com/seckillnew/orderService/init.action",
                data,
                headers,
            )
        except Exception as e:
            print(str(e))
            return None

        # process response

        return response

    def get_tak(self, ua, s, get_sk):
        headers = {ua}
        respond = s.get("https://tak.jd.com/a/tr.js?_t=2685900", headers=headers)
        respond_text = respond.text
        pattern = re.compile(r"var sk = \"(.*?)\";")
        sk = pattern.findall(respond_text)[0]
        return sk

    def submit_order(self, order_data, sk, num):
        return None

    def send_message(self, content):
        return None


if __name__ == "__main__":
    ck = ZCSUPER_cookie
    jdapi = JDSecKillAPI(zcsuper_sku, ck)
    prom_date = jdapi.appoint_sku()
    json_data = json.dumps(json_data)
    title = json_data["title"]
    print("gentoken结果--->")
    jdapi.get_token_key()
    print("预约结果--------------------------", title)
