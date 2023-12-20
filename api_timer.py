# Source Generated with Decompyle++
# File: api_timer.pyc (Python 3.9)

import time
import datetime
import requests


class JDTimer:
    def __init__(self):
        self.headers = {
            "user-agent": "okhttp/3.12.1;jdmall;android;version/10.5.0;build/95837;",
            "content-type": "application/x-www-form-urlencoded",
        }
        self.session = requests.Session()
        try:
            self.jd_time()
        except Exception as e:
            print("api_timer.py", e)

    def jd_time(self):
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

    def local_time(self):
        """
        获取本地时间戳
        """
        local_timestamp = round(time.time() * 1000)
        return local_timestamp

    def local_jd_time_diff(self):
        """
        计算本地与京东服务器时间差
        """
        start_time = time.time()
        jd_timestamp = self.jd_time()
        end_time = time.time()
        local_timestamp = round(((start_time + end_time) / 2) * 1000)
        time_diff = local_timestamp - jd_timestamp
        print("本地时间: ", datetime.datetime.fromtimestamp(local_timestamp / 1000))
        print("京东时间: ", datetime.datetime.fromtimestamp(jd_timestamp / 1000))
        print("误差毫秒数: ", time_diff)
        return time_diff


if __name__ == "__main__":
    jdtimer = JDTimer()
    for i in range(4):
        print(jdtimer.local_jd_time_diff())
