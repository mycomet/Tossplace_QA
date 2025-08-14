# 로그인 화면 내 기능 (pages/tossplace_page.py)

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

class TossplacePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login_entry(self):  # 최초 화면에서 로그인하기 버튼
        btn = self.wait.until(lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("로그인 하기")'))
        btn.click()

    def click_phone_login(self):  # 로그인 하기 진입 후 휴대폰 번호 로그인
        btn = self.wait.until(lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("휴대폰 번호 로그인")'))
        btn.click()

    def input_info(self, num, pw):  # 폰번호, 비번 입력
        input_box = self.driver.find_elements(AppiumBy.CLASS_NAME, 'android.widget.EditText')
        input_box[0].send_keys(num)
        input_box[1].send_keys(pw)

    def empty_space(self):  # 빈공간 누르기 (키패드 내리기용)
        btn = self.wait.until(lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.ListView")'))
        btn.click()

    def click_login_button(self):  # 로그인 시도 버튼
        btn = self.wait.until(lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("로그인")'))
        btn.click()

    def get_error_message(self):  # 에러 메시지 가져오기
        try:
            error = self.wait.until(lambda d: d.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().textContains("ID를 확인해 주세요")'))
            return error.text
        except:
            return None

    def is_home_displayed(self):  # 홈화면 진입 확인
        return "홈 화면" in self.driver.page_source
