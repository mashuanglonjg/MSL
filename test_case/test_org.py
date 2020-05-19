from conftest import browser
import pytest
from page.orgapply import Joinorgpage
from page.login import Loginpage
import allure


@allure.feature('demo')
class TestLogin():
    """机构申请"""
    def test_org(self, browser):
        org_page = Loginpage(browser).admin_login('18888888888', 'test1234').add_apply()
        org_page.org_apply()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_org.py"])