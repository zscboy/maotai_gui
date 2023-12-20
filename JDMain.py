import warnings
import time
import datetime
import jdseckillAPIv2
from jdseckillAPIv2 import JDSecKillAPI
import tools.mylogger as logger


class JDSecKillSubmit:
    def __init__(self, sku, ck):
        super().__init__()
        self.sku = sku
        self.ck = ck
        self.QTextEdit = None

    def setLogText(self, QTextEdit):
        self.QTextEdit = QTextEdit

    def log(self, str_p):
        logger.info(str_p)

    def appoint_task(self):
        try:
            resp_json = self.appoint_sku()
            self.log("appoint_task:" + str(resp_json))
            return resp_json
        except Exception as e:
            print(str(e))

    def killSku(self, killTimeTs):
        token_params = jdseckillAPIv2.JDSecKillAPI.get_token_key()
        divide_url = jdseckillAPIv2.JDSecKillAPI.get_divide(token_params)
        captcha_url = jdseckillAPIv2.JDSecKillAPI.get_captcha(token_params)
        seckill_url = jdseckillAPIv2.JDSecKillAPI.visit_seckill(killTimeTs)
        resp = jdseckillAPIv2.JDSecKillAPI.get_tak()
        order_data = jdseckillAPIv2.JDSecKillAPI.submit_order(
            token_params, seckill_url, resp
        )
        nowTimeTs = int(time.time() * 1000)
        sk_val = jdseckillAPIv2.JDSecKillAPI.send_message(
            token_params, seckill_url, order_data, nowTimeTs
        )
        resp_json = jdseckillAPIv2.JDSecKillAPI.init_action(
            token_params, seckill_url, order_data, nowTimeTs, sk_val
        )
        txt = jdseckillAPIv2.JDSecKillAPI.get_appjmp(
            token_params, seckill_url, resp_json
        )

        try:
            while True:
                if datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"):
                    break
                time.sleep(0.01)

            resp_json_final = jdseckillAPIv2.JDSecKillAPI.submit_order(
                token_params, seckill_url, resp_json
            )
            return resp_json_final

        except Exception as e:
            print(str(e))
