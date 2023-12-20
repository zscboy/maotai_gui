# Source Generated with Decompyle++
# File: config_function.pyc (Python 3.9)

import configparser
import os


def read_config(cookie_type=(None,)):
    config = configparser.ConfigParser()
    with open(
        os.path.join(os.getcwd(), "config.ini"), "r", "utf-8-sig", **("encoding",)
    ) as f:
        config.read_file(f)
    zcsuper_cookie = config.get("DEFAULT", "zcsuper_Cookie", raw=True)
    zcsuper_key = config.get("DEFAULT", "zcsuper_key")
    zcsuper_uuid = config.get("DEFAULT", "zcsuper_uuid")
    zcsuper_eid = config.get("DEFAULT", "zcsuper_eid")
    zcsuper_uts = config.get("DEFAULT", "zcsuper_uts")
    zcsuper_area = config.get("DEFAULT", "zcsuper_area")
    zcsuper_sku = config.get("DEFAULT", "zcsuper_sku")
    zcsuper_user_killTime = config.get("DEFAULT", "zcsuper_user_killTime")
    return (
        zcsuper_cookie,
        zcsuper_key,
        zcsuper_uuid,
        zcsuper_eid,
        zcsuper_uts,
        zcsuper_area,
        zcsuper_sku,
        zcsuper_user_killTime,
    )


read_config()
