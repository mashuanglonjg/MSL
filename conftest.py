import os
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options as CH_Options
from selenium.webdriver.firefox.options import Options as FF_Options
from config import RunConfig
import allure

driver = None

# 定义基本测试环境
@pytest.fixture(scope='function')
def base_url():
    return RunConfig.url

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        with allure.step('点击查看失败截图'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)

# 启动浏览器
@pytest.fixture(scope='class', autouse=True)
def browser():
    """
    全局定义浏览器驱动（注意chrome版本要和chrome driver版本匹配）
    :return:
    """
    global driver

    if RunConfig.driver_type == "chrome":
        # 本地chrome浏览器
        driver = webdriver.Chrome()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome_pad":
        # 学生按分辨率启动
        WIDTH = 960
        HEIGHT = 600
        PIXEL_RATIO = 3.0
        UA = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
        mobileEmulation = {"deviceMetrics": {"width": WIDTH, "height": HEIGHT, "pixelRatio": PIXEL_RATIO},
                           "userAgent": UA}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        driver = webdriver.Chrome(chrome_options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)

    elif RunConfig.driver_type == "firefox":
        # 本地firefox浏览器
        driver = webdriver.Firefox()
        driver.maximize_window()

    elif RunConfig.driver_type == "chrome-headless":
        # chrome headless模式
        chrome_options = CH_Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif RunConfig.driver_type == "firefox-headless":
        # firefox headless模式
        firefox_options = FF_Options()
        firefox_options.headless = True
        driver = webdriver.Firefox(firefox_options=firefox_options)

    elif RunConfig.driver_type == "grid":
        # 通过远程节点运行
        driver = Remote(command_executor='http://localhost:4444/wd/hub',
                        desired_capabilities={
                            "browserName": "chrome",
                        })
        driver.set_window_size(1920, 1080)

    else:
        raise NameError("driver驱动类型定义错误！")

    return driver


# 关闭浏览器
@pytest.fixture(scope="class", autouse=True)
def browser_close():
    yield driver
    driver.quit()
    print("测试结束！")


if __name__ == "__main__":
    capture_screenshots("test_dir/test_baidu_search.test_search_python.png")
