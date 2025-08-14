# tests/conftest.py
import pytest
import time
from appium import webdriver
from config import get_driver_options

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Remote("http://localhost:4723", options=get_driver_options())

    # 앱 강제종료 후 실행
    driver.terminate_app("com.tossplace.app.release")
    driver.activate_app("com.tossplace.app.release")
    time.sleep(10)

    yield driver

    time.sleep(10)

    driver.quit()