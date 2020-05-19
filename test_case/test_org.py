from conftest import browser
import pytest
from page.login import Loginpage
import allure


@allure.feature('机构申请')
class TestOrg():
    """机构申请"""
    def test_org(self, browser):
        org_page = Loginpage(browser).user_login('15905190001', 'test1234').org()
        org_page.org_apply()
        org_page.org_pass()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_org.py"])