# -*- coding: utf-8 -*-
# @ModuleName: app
# @Time: 2023/08/07 11:07
# @Author     : WangPengDa
# @Description:
# @Software   : PyCharm
import configparser
import logging
import os
import sys

import requests
from requests.exceptions import RequestException

CURRENT_PATH = os.path.dirname(os.path.realpath(sys.argv[0]))


def init_conf():
    conf_path = os.path.join(CURRENT_PATH, "conf.ini")
    if not os.path.exists(conf_path):
        config = open(conf_path, "w")
        config.write("[config]\n")
        config.write("base_url = http://127.0.0.1:32251/\n")
        config.write("secret_key = default\n")
        config.close()
        return "http://127.0.0.1:32251/", "default"
    config = configparser.ConfigParser()  # 类实例化

    config.read(conf_path)
    return config["config"]["base_url"], config["config"]["secret_key"]


def init_logger():
    log_path = os.path.join(CURRENT_PATH, "log")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
    formator = logging.Formatter(fmt="[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] %(message)s")
    fh = logging.FileHandler(os.path.join(log_path, "app.log"), encoding="utf-8")
    logger.addHandler(fh)
    fh.setFormatter(formator)
    return logger


def main():
    logger = init_logger()
    BASE_URL, secret_key = init_conf()

    url = BASE_URL + "upload/"
    img_list = sys.argv
    img_list.pop(0)

    for img in img_list:
        img_data = open(img, "rb")
        try:
            header = {
                "Secret-Key": secret_key
            }
            result = requests.post(url, files={"img": img_data}, headers=header).json()
            if result.get("success"):
                data = result.get("data")
                logger.info("result =====> " + str(data))
                for img_name in data:
                    print(BASE_URL + "get-img/" + img_name)
            else:
                if result.get("code") == 403:
                    logger.warning("上传错误，检查服务端与客户端密钥是否一致")
        except RequestException:
            logger.warning("上传错误，检查服务端是否启动")
        finally:
            img_data.close()
    if not img_list:
        logger.error(f"上传错误，参数为{img_list}")


if __name__ == '__main__':
    main()
