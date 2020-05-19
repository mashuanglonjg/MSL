from conftest import browser
import pytest
from page.login import Loginpage
import allure


@allure.feature('机构申请')
class TestOrg():
    """机构申请"""
    def test_org(self, browser):
<<<<<<< HEAD
        org_page = Loginpage(browser).admin_login('18888888888', 'test1234').add_apply()
=======
        org_page = Loginpage(browser).user_login('15905190001', 'test1234').org()
>>>>>>> 0d68df74523f0c5736fec808c8736d31b8e2f46a
        org_page.org_apply()
        org_page.org_pass()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_org.py"])