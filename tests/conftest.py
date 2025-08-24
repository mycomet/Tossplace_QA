
import pytest
import subprocess
import time
import os
import signal
import psutil
from appium import webdriver
from config import get_driver_options  # 네가 만든 config.py에서 driver 옵션 가져오기


@pytest.fixture(scope="session")
def appium_server():
    """Appium 서버를 실행하고, 테스트가 끝나면 종료"""
    appium_path = r"C:\Users\kyuhyun.choi\AppData\Roaming\npm\appium.cmd"

    # Appium 서버 실행
    server = subprocess.Popen(
        [appium_path, "--allow-cors"],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
    print("📡 Appium 서버 실행 중... 대기")
    time.sleep(5)

    yield  # 👉 여기서 테스트들이 실행됨

    print("🛑 Appium 서버 종료 중...")
    try:
        if psutil.pid_exists(server.pid):
            if os.name == "nt":
                subprocess.run(["taskkill", "/F", "/PID", str(server.pid)], check=True)
            else:
                os.kill(server.pid, signal.SIGTERM)
            print("✅ Appium 서버 종료 완료")
        else:
            print("⚠ Appium 서버가 이미 종료된 상태")
    except Exception as e:
        print(f"⚠ 서버 종료 실패: {e}")


@pytest.fixture(scope="session")
def driver(appium_server):
    """Appium driver 생성 및 종료"""
    driver = webdriver.Remote("http://127.0.0.1:4723", options=get_driver_options())
    
    driver.terminate_app("com.tossplace.app.release")
    driver.activate_app("com.tossplace.app.release")
    
    time.sleep(10)
    
    yield driver
    
    time.sleep(10)
    
    driver.quit()