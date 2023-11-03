import pymysql
from dbutils.pooled_db import PooledDB
from pymysql import cursors
from common.config import conf


class Pool(object):
    __pool = None
    __MAX_CONNECTIONS = 100  # 创建连接池的最大数量
    __MIN_CACHED = 10  # 连接池中空闲连接的初始数量
    __MAX_CACHED = 20  # 连接池中空闲连接的最大数量
    __MAX_SHARED = 0  # 池中共享连接的最大数量 默认为0，即每个连接都是专用的，不可共享(不常用，建议默认)
    __BLOCK = True  # 超过最大连接数量时候的表现，为True等待连接数量下降，为false直接报错处理
    __MAX_USAGE = 0  # 单个连接的最大重复使用次数，默认是0
    __RESET = True  # 当连接返回到池中时，重置连接的方式。默认True，总是执行回滚
    __SET_SESSION = ["SET AUTOCOMMIT = 1"]  # 设置自动提交

    def __init__(self, host, port, user, password, database):
        if not self.__pool:
            self.__class__.__pool = PooledDB(
                creator=pymysql,
                host=host,
                port=port,
                user=user,
                password=password,
                database=database,
                maxconnections=self.__MAX_CONNECTIONS,
                mincached=self.__MIN_CACHED,
                maxcached=self.__MAX_CACHED,
                maxshared=self.__MAX_SHARED,
                blocking=self.__BLOCK,
                maxusage=self.__MAX_USAGE,
                setsession=self.__SET_SESSION,
                reset=self.__RESET,
                charset="utf8mb4",
            )

    def get_connect(self):
        return self.__pool.connection()


pool = connects_pool = Pool(
    host=conf.get_by_name("mysql.host"),
    port=conf.get_by_name("mysql.port"),
    user=conf.get_by_name("mysql.user"),
    password=conf.get_by_name("mysql.password"),
    database=conf.get_by_name("mysql.database"),
)


class DB(object):
    def __enter__(self):
        connect = pool.get_connect()
        cursor = connect.cursor(cursors.DictCursor)
        # https://blog.51cto.com/abyss/1736844
        # connect.autocommit = False # 如果使用连接池 则不能在取出后设置 而应该在创建线程池时设置
        self._connect = connect
        self._cursor = cursor
        return cursor

    """
    这三个值用于描述在上下文块中发生的异常：
        exc_type：表示异常的类型，通常是异常类的引用，例如 ValueError 或 TypeError。
        exc_value：表示引发的异常实例，通常包含异常的详细信息，例如异常消息。
        traceback：表示异常的回溯（traceback）对象，包含了关于异常的详细堆栈信息，可以用于调试。
    """

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self._connect.rollback()
        else:
            self._connect.commit()
        self._cursor.close()
        self._connect.close()

    @property
    def cursor(self):
        return self._cursor


if __name__ == "__main__":
    with DB() as db:
        db.execute("select * from `activities`")
        res = db.fetchone()
        print(res)
