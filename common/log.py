import logging
from logging.handlers import TimedRotatingFileHandler
from common.config import conf
from common.tool import parse_log_level
import os

path = os.path.dirname(os.path.dirname(__file__))


class Log(object):
    def __init__(
        self,
        filename="test.txt",
        level=logging.INFO,
        is_add_default_handler=True,
        is_console=True,
    ):
        # 获取 logger 实例
        logger = logging.getLogger(filename)
        logger.setLevel(level)

        filepath = os.path.join(path, f"logs")
        # 创建目录
        # 需要注意：如果 python 是 logs/text.log
        # 那么 makedirs 会将 text.log 也创建成目录而不是文件
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        self.logger = logger
        self.level = level
        self.filepath = os.path.join(filepath, filename)
        self.filename = filename

        # 设置日志处理句柄
        if is_add_default_handler:
            self.__default_handler()

    def __default_handler(self):
        handler = TimedRotatingFileHandler(
            self.filepath, when="D", interval=1, backupCount=7
        )
        handler.suffix = "%Y-%m-%d.log"
        handler.setLevel(self.level)

        # 设置格式化
        handler.setFormatter(self.__get_default_format())

        self.logger.addHandler(handler)

    @classmethod
    def __get_default_format(cls):
        formatter = logging.Formatter(
            "%(asctime)s - %(filename)s - %(module)s - %(funcName)s[:%(lineno)d] - %(levelname)s - %(message)s"
        )
        return formatter

    def set_handler(self, handler):
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


log = Log(
    level=parse_log_level(conf.get_by_name("log.level")),
    filename=conf.get_by_name("log.filename"),
).get_logger()


if __name__ == "__main__":
    log.info("121")
