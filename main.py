# main.py
import subprocess
import time
import pytest
import os
import signal

if __name__ == "__main__":
    # Appium 경로 설정
    appium_path = "C:\\Users\\kyuhyun.choi\\AppData\\Roaming\\npm\\appium.cmd"

    # Appium 서버 실행
    appium_server = subprocess.Popen(
        [appium_path, "--allow-cors"],
        creationflags=subprocess.CREATE_NEW_CONSOLE)

    try:
        print("📡 Appium 서버 실행 중... 대기 중...")
        time.sleep(5)  # 서버 안정화 대기

        # pytest 실행 (로그도 출력되도록 -s 옵션)
        print("🚀 테스트 실행 시작!")
        pytest.main(["-s", "tests/test_login.py"])

    finally:
        print("🛑 Appium 서버 종료 중...")
        # 서버 종료 (윈도우면 os.kill 안 먹힐 수 있어서 따로 설명해줄게)
        try:
            os.kill(appium_server.pid, signal.SIGTERM)
        except Exception as e:
            print(f"⚠ 서버 종료 실패: {e}")
