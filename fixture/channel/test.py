import pytest
@pytest.fixture(scope="function")
def fixture_driver(driver):
    print("开始执行测试用例")
    yield driver
    print("结束执行测试用例")