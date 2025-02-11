import pytest
from common.driver import Driver

@pytest.fixture(scope="function")
def driver():
    """全局 WebDriver 实例"""
    driver_instance = Driver().get_instance()
    driver_instance.current_test_case = None  # 初始化
    yield driver_instance
    driver_instance.quit()
