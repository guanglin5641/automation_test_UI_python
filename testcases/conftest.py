from common.driver import Driver
import pytest
from common.tool import add_image_attach, function_description

instance = None


@pytest.fixture()
def driver():
    global instance
    instance = Driver().get_instance()
    yield instance
    instance.quit()


# 此钩子函数会在测试用例执行的不同阶段（setup, call, teardown）都会调用一次
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # 获取钩子方法的调用结果
    out = yield
    # 从钩子方法的调用结果中获取测试报告
    report = out.get_result()

    if report.when == "call":
        # 当测试用例失败时，则截图
        if report.failed:
            image_name = "测试用例失败"
            function_doc = item.function.__doc__
            if function_doc:
                image_name = function_description(function_doc)
            add_image_attach(instance, image_name)
