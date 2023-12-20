import time

from redis import StrictRedis
from common.config import conf

redis = StrictRedis(
    host=conf.get_by_name("redis.host"),
    port=conf.get_by_name("redis.port"),
    db=conf.get_by_name("redis.db"),
    password=conf.get_by_name("redis.password"),
    encoding="utf-8",
    # 自动将从 Redis 服务器获取的二进制数据解码为字符串
    # 这在处理文本数据时非常方便，因为无需手动进行解码操作
    decode_responses=True,
)


# CasesProgress 测试进度
class CasesProgress(object):
    def __init__(self):
        self.redis_client = redis
        self.UI_AUTOTEST_PROCESS = "ui_autotest_process"  # hash 结构
        self.FAILED_TESTCASES_NAMES = "failed_testcase_name"  # 列表接口，存储所有失败的 case
        self.RUNNING_STATUS = "running_status"  # 当前运行的状态：1运行中0停止

    # 重置
    def reset(self):
        # 删除所有进度
        self.redis_client.delete(self.UI_AUTOTEST_PROCESS)
        # 删除所有失败用例的名称
        self.redis_client.delete(self.FAILED_TESTCASES_NAMES)

    def init_process(self, total: str):
        """
        初始化进度，包括总数、成功数、失败数、开始时间、运行状态
        :param total:
        :return:
        """
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "total", total)
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "success", "0")
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "fail", "0")
        self.redis_client.hset(
            self.UI_AUTOTEST_PROCESS, "start_time", str(int(time.time() / 1000))
        )
        self.redis_client.hset(self.UI_AUTOTEST_PROCESS, "end_time", "")
        self.redis_client.set(self.RUNNING_STATUS, 1)

    def update_success(self):
        """
        成功用例个数+1
        :return:
        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "success")

    def update_fail(self):
        """
        失败用例个数+1
        :return:
        """
        self.redis_client.hincrby(self.UI_AUTOTEST_PROCESS, "fail")

    def insert_into_fail_testcase_name(self, fail_testcase_name):
        """
        增加失败用例名称
        :param fail_testcase_name:
        :return:
        """
        self.redis_client.lpush(self.FAILED_TESTCASES_NAMES, fail_testcase_name)

    def get_result(self):
        """
        获取测试结果
        :return:
        """
        total = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "total")
        if total is None:
            total = 0
        success = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "success")
        if success is None:
            success = 0
        fail = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "fail")
        if fail is None:
            fail = 0
        start_time = self.redis_client.hget(self.UI_AUTOTEST_PROCESS, "start_time")
        if start_time is None:
            start_time = ""
        return int(total), int(success), int(fail), start_time

    def get_process(self):
        """
        获取测试进度，计算百分比
        :return:
        """
        total, success, fail, _ = self.get_result()
        if total == 0:
            return 0
        else:
            return "%.1f" % ((int(success) + int(fail)) / int(total) * 100) + "%"

    def get_fail_testcase_names(self):
        """
        获取所有失败的用例名称
        :return:
        """
        fail_testcase_names = self.redis_client.lrange(
            self.FAILED_TESTCASES_NAMES, 0, -1
        )
        return fail_testcase_names

    def write_end_time(self):
        """
        把测试结束时间写入redis
        :return:
        """
        self.redis_client.hset(
            self.UI_AUTOTEST_PROCESS, "end_time", str(int(time.time() * 100))
        )

    def modify_running_status(self, status):
        """
        修改运行状态
        :param status:
        :return:
        """
        if status not in [1, 0]:
            status = 0
        self.redis_client.set(self.RUNNING_STATUS, status)
