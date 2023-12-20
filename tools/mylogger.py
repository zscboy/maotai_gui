# decompyle3 version 3.9.0
# Python bytecode version base 3.8.0 (3413)
# Decompiled from: Python 3.8.13 (default, Mar 28 2022, 06:59:08) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: jd\tools\mylogger.py
import logging
import logging.handlers
import os
from datetime import datetime

file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))

new_path = os.path.join(dir_path, "log")
# print(os.getcwd())
if not os.path.exists(new_path):
    os.makedirs(new_path)
now = datetime.now()
# formatted_time = now.strftime("%Y-%m-%d-%H-%M-%S")
formatted_time = now.strftime("%Y-%m-%d")
LOG_FILENAME = "jd-" + formatted_time + ".log"
LOG_PATH = os.path.join(new_path, LOG_FILENAME)

# root logger 可以log所有logger输出的信息
logger = logging.getLogger()
# logger = logging.getLogger('jd_maotai')
print("log所在目录：" + LOG_PATH)


def set_logger():
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        file_handler = logging.handlers.RotatingFileHandler(
            LOG_PATH, maxBytes=5242880, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def setting_logger(logger_new):
    if not logger_new.handlers:
        logger_new.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger_new.addHandler(console_handler)
        path_new = os.path.join(new_path, formatted_time)
        if not os.path.exists(path_new):
            os.makedirs(path_new)
        path_logger_new = os.path.join(path_new, logger_new.name + ".log")
        file_handler = logging.handlers.RotatingFileHandler(
            path_logger_new, maxBytes=5242880, backupCount=5, encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger_new.addHandler(file_handler)


set_logger()
# okay decompiling mylogger.pyc
