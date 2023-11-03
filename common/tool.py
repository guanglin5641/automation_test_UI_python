import time

import allure

import logging


def parse_log_level(level: str):
    d = {
        "FATAL": logging.CRITICAL,
        "CRITICAL": logging.CRITICAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "WARN": logging.WARNING,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET,
    }
    level = level.upper()
    if level not in d:
        return logging.INFO
    return d[level]


def function_description(input_string: str):
    parts = input_string.split(":param", 1)
    return parts[0].strip()


def add_image_attach(driver, step_name, sleep=0.5):
    """
    添加附件到测试报告中
    :param driver:
    :param step_name:
    :param sleep:
    :return:
    """
    if sleep > 0:
        time.sleep(sleep)
    # 第一个参数是附件的内容
    # 第二个参数是附件的名称
    # 第三个参数是附件的类型
    allure.attach(
        driver.get_screenshot_as_png(),
        f"{step_name}.png",
        allure.attachment_type.PNG,
    )


if __name__ == "__main__":
    # 您的输入字符串
    s = """登录测试用例"""
    print(function_description(s))
