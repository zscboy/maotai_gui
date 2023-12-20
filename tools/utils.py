import hashlib
import platform
import random
import socket
from datetime import datetime
import sys
import os
from http.cookies import SimpleCookie
import json
import re
from tools.ModifiedBase64 import ModifiedBase64


def text_to_json(text, regex):
    pattern = re.compile(regex)
    text_list = pattern.findall(text)
    _json = json.loads(text_list[0])
    return _json


def remove_unused_symbol(text):
    text = text.replace("\n", "").replace("\r", "").replace("\t", "")
    return text


def remove_redundant_comma(text):
    rex = r'(?<=[}\]"\'])\s*,\s*(?!\s*[{["\'])'
    text = re.sub(rex, "", text)
    return text


def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath("..\\..")
    return os.path.join(base_path, relative_path)


def export_file_name():
    return "ck-export-" + datetime.now().strftime("%Y%m%d%H%M%S") + ".txt"


def desktop_path():
    if platform.system() == "Windows":
        return "C:\\Users\\Administrator\\Desktop"
    else:
        return "/Users/xiaoqingsong/Desktop"


def is_json(text):
    if text is None:
        return False
    try:
        json.loads(text)
        return True
    except ValueError:
        return False


def getTimeStamp(time):
    ts = datetime.timestamp(datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f"))
    return int(ts * 1000)


def getTimeStamp(format, time):
    ts = datetime.timestamp(datetime.strptime(time, format))
    return int(ts * 1000)


def getNowTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-7]


def getCookieFromStr(rawStr):
    cookie = SimpleCookie()
    cookie.load(rawStr)

    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value

    return cookies


def get_random_number_str(length):
    return "".join(str(random.choice(range(10))) for _ in range(length))


def randomUUID():
    random_number = get_random_number_str(15)
    random_str = hashlib.md5(random_number.encode("utf-8")).hexdigest()[:12]
    return random_number + "-" + random_str


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = None
    return ip


def mb_encrypt(str):
    v = ModifiedBase64()
    return v.m23207r(str)


def get_ep(ts, uuid):
    area = "13_1000_40488_54435"
    d_model = "PDNM00"
    wifiBssid = "unknown"
    osVersion = "11"
    d_brand = "OPPO"
    screen = "2161*1080"
    aid = uuid
    openudid = uuid
    hdid = ""

    hdid = mb_encrypt(hdid)
    ts = mb_encrypt(ts)
    area = mb_encrypt(area)
    d_model = mb_encrypt(d_model)
    wifiBssid = mb_encrypt(wifiBssid)
    osVersion = mb_encrypt(osVersion)
    d_brand = mb_encrypt(d_brand)
    screen = mb_encrypt(screen)
    uuid = mb_encrypt(uuid)
    aid = mb_encrypt(aid)
    openudid = mb_encrypt(openudid)

    ep = {
        "area": area,
        "d_model": d_model,
        "wifiBssid": wifiBssid,
        "osVersion": osVersion,
        "d_brand": d_brand,
        "screen": screen,
        "uuid": uuid,
        "aid": aid,
        "openudid": openudid,
    }

    ep = ep[:5]
    ep[5] = "1.2.0"
    ep["appname"] = "com.jingdong.app.mall"

    return ep
