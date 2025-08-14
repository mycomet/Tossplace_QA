import pytest
from pages.tossplace_page import TossplacePage
from utils.spass_handler import handle_Spass
from selenium.common.exceptions import TimeoutException

# 공통 로그인 시나리오 함수
def login_flow(driver, phone, password, step):
    page = TossplacePage(driver)
    
    if step == 1:
        page.click_login_entry()
        page.click_phone_login()
        handle_Spass(driver)
        page.empty_space() # 키패드 제거
        page.input_info(phone, password)
    
    elif (step == 2 or 3):
        page.click_phone_login()
        page.input_info(phone, password)
    
    else:
        page.click_phone_login()
        page.input_info(phone, password)
        
    page.click_login_button()
    handle_Spass(driver)
    print(f"TC{step} 완료")
    return page


# 로그인 Test Case
@pytest.mark.parametrize("phone,password,expected_error,step",
    [
    ("", "", None, 1),              # 케이스1: 아무것도 입력 안함
    ("01011112222", "", None, 2),   # 케이스2: 비번 없음
    ("", "1234", None, 3),          # 케이스3: 비번만 입력
    ("01023542476", "qqqaaa", "ID를 확인해 주세요", 4)  #케이스4 : 틀린ID, 틀린pw 입력
    ])


def test_login(driver, phone, password, expected_error, step):
    page = login_flow(driver, phone, password, step)
    
    if expected_error:
        assert page.get_error_message() == expected_error
    else:
        assert page.get_error_message() is None