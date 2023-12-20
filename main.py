import requests
import time
import sys
import os
import re
import datetime
import threading
from datetime import timedelta
from config_function import read_config
from tools.mylogger import logger
import uuid
from tools import utils
from JDMain import JDSecKillSubmit
from api_timer import JDTimer

# def get_mac_address():
#     mac = uuid.getnode()
#     mac_address = None((lambda .0 = None: [ '{:02x}'.format(mac >> i & 255) for i in .0 ])(range(0, 48, 8)))
#     return mac_address


def get_mac_address():
    mac = uuid.getnode()
    mac_address = ":".join(
        ["{:02x}".format((mac >> i) & 0xFF) for i in range(0, 48, 8)][::-1]
    )
    return mac_address


mac_address = get_mac_address()
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


timeDiff = 0


def syncTime():
    jdTimer = JDTimer()
    return jdTimer.local_jd_time_diff()


def threa_sum(sums):
    return sums


def yuyueSku(sku, ck):
    jdapi = JDSecKillSubmit(sku, ck)
    relus = jdapi.appoint_task()
    return relus


def get_GonGao():
    GET_GG = requests.get("https://docs.zcsuper.cn/python/gg_config.json")
    gg_info = GET_GG.json()
    notice = gg_info["notice"]
    guangb = gg_info["guangb"]
    weihu = gg_info["weihu"]
    return (notice, guangb, weihu)


def killSku(sku, ck, killTimeTs):
    jdapi = JDSecKillSubmit(sku, ck)
    for i in range(10):
        print(f"""第{i}次抢购结果""")
        if jdapi.killSku(killTimeTs):
            pass

        return None


def work(killTime, ck, sku):
    killTimeTs = utils.getTimeStamp(killTime, "%Y-%m-%d %H:%M:%S.%f", **("format",))
    syncedTime = False
    nowTimeTs = int(time.time() * 1000)
    killDiff = killTimeTs - nowTimeTs
    if not killDiff < 300000 and syncedTime:
        syncedTime = True
        timeDiff = syncTime()
        print("时差：%s" % str(timeDiff))
        killTimeTs = killTimeTs + timeDiff
    elif killDiff < 0:
        print("时差：%s" % str(timeDiff))
        killSku(sku, ck, killTimeTs, **("sku", "ck", "killTimeTs"))
    else:
        time.sleep(0.01)


def yuyue_work(killTime, ck, sku):
    killTimeTs = utils.getTimeStamp(killTime, "%Y-%m-%d %H:%M:%S.%f", **("format",))
    hasYuyue = False
    nowTimeTs = int(time.time() * 1000)
    killDiff = killTimeTs - nowTimeTs
    if not killDiff < 60000 and hasYuyue:
        hasYuyue = True
        startmin = yuyueSku(sku, ck, **("sku", "ck"))
        print("距离开抢时间不足三十分钟，正在预约：", startmin)
        return None
    time.sleep(0.01)


def extract_pin(input_string):
    pattern = "pin=(.*?);"
    match = re.search(pattern, input_string)
    if match:
        return match.group(1)
    return None


def adjust_time(killTime, timeDiff):
    print("设定的秒杀时间：", killTime)
    dt = datetime.datetime.strptime(killTime, "%H:%M:%S:%f")
    if timeDiff >= 0:
        adjusted_dt = dt + timedelta(abs(timeDiff), **("milliseconds",))
    else:
        adjusted_dt = dt - timedelta(abs(timeDiff), **("milliseconds",))
    adjusted_time_str = adjusted_dt.strftime("%H:%M:%S.%f")[:-3]
    adujusted_time_int = adjusted_time_str
    print("根据误差修正后的时间：", adujusted_time_int)
    return adjusted_time_str


if __name__ == "__main__":
    (
        zcsuper_cookie,
        zcsuper_key,
        zcsuper_uuid,
        zcsuper_eid,
        zcsuper_uts,
        zcsuper_area,
        zcsuper_sku,
        zcsuper_user_killTime,
    ) = read_config()
    current_date = datetime.datetime.now().date()
    kill_time = datetime.time(
        12, 0, 0, 0, **("hour", "minute", "second", "microsecond")
    )
    # (GG_announcement, guangb, weihu) = get_GonGao()
    # isRun = False
    # card_info = {"vip": False, "maintenance": weihu, "end_time": ""}
    # get_url = "http://154.12.37.177:5000/get-key-info"
    # params = {"key": zcsuper_key}
    # response = requests.get(get_url, params, **("params",))
    # vip_value = False
    # end_times = ""
    # if response.status_code == 200:
    #     data = response.json()
    #     vip_value = data.get("vip")
    #     end_times = data.get("end_time")
    # else:
    #     print("请求失败，HTTP 状态码为：", response.status_code)
    # card_info["vip"] = vip_value
    # card_info["end_time"] = end_times
    # if card_info["maintenance"]:
    #     logger.info("服务停机维护中...")
    #     logger.info(f"""维护原因：{guangb}""")
    #     input("按下Enter键退出")
    # elif card_info["vip"]:
    #     logger.info("VIP特权通道")
    #     isRun = True
    # else:
    #     url = "http://154.12.37.177:5000/check_key"
    #     params = {
    #         "key": zcsuper_key if zcsuper_key is not None else "123",
    #         "JD_name": extract_pin(zcsuper_cookie),
    #         "ddcode": mac_address,
    #     }
    #     response = requests.post(url, params, **("data",))
    #     if response.status_code == 200:
    #         result = response.json()
    #         if result["code"] == 200:
    #             logger.info(result["message"])
    #             isRun = True
    #         elif result["code"] == 404:
    #             logger.info(result)
    #             input("按下Enter键退出")
    #         else:
    #             logger.info("请求失败，HTTP 状态码为：", response.status_code)
    #             input("按下Enter键退出")
    isRun = True
    if isRun:
        current_time = datetime.datetime.now().time()
        if current_time < datetime.time(12, 30, 30, **("hour", "minute", "second")):
            target_datetime = datetime.datetime.combine(current_date, kill_time)
        else:
            next_date = current_date + datetime.timedelta(1, **("days",))
            target_datetime = datetime.datetime.combine(next_date, kill_time)
        target_microsecond = target_datetime.microsecond // 1000
        target_time_str = (
            target_datetime.strftime("%Y-%m-%d")
            + f""" {adjust_time('11:59:59:999', syncTime())}"""
        )
        if zcsuper_user_killTime != "":
            (year_M_D, min_H_s) = zcsuper_user_killTime.split(" ")
            target_time_str = year_M_D + f""" {adjust_time(min_H_s, syncTime())}"""
        killTime = target_time_str
        cks = [zcsuper_cookie]
        print("开始校验Cookie...")
        logger.info("开始校验Cookie...")
        rule_cookie = yuyueSku(zcsuper_sku, zcsuper_cookie, **("sku", "ck"))
        if rule_cookie["code"] == "1":
            logger.info("登录失败，当前状态：您的Cookie或其他参数有误！")
        else:
            print("校验成功...")
            print("本次执行时间：", killTime)
            threads = []
            yuyue_work(killTime, zcsuper_cookie, zcsuper_sku)
            for i in range(14):
                t = threading.Thread(
                    work,
                    (killTime, cks[i % len(cks)], zcsuper_sku),
                    **("target", "args"),
                )
                t.start()
                threads.append(t)
            print("等待执行")
            for t in threads:
                t.join()
            print("执行完毕！")
        input("按下Enter键退出")
