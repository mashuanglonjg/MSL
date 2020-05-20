from conftest import browser
import pytest
from page.login import Loginpage
from util.MysqlUtil import MysqlUtil
import allure


@allure.feature('机构申请')
class TestOrg():
    """机构申请"""
    def test_org(self, browser):
        org_page = Loginpage(browser).user_login('15905190001', 'test1234').org()
        org_page.org_apply()

    def test_pass(self):
        """
        后台审核通过+角色变化
        :return:
        """
        db = MysqlUtil()
        userid = db.fetchone("select userid from lt_user where isDeleted = 0 and phone = 15905190001;")
        orgid = db.fetchone("select id from lt_org where isDeleted = 0 and name = 'UI自动化机构名称';")
        db = MysqlUtil.getConnect(self)
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute("UPDATE lt_org set status = 2 where name = 'UI自动化机构名称' and isDeleted = 0;")
            cursor.execute("UPDATE lt_user set roleId = 101 where isDeleted = 0 and userid = " + str(userid[0]) +  ";")
            cursor.execute("INSERT INTO lt_org_teacher_mapping(userId, orgId, userName, summary, photo, isDeleted, createdOn, createdBy, modifiedOn, modifiedBy) VALUES (" + str(userid[0]) + ", " + str(orgid[0]) + ", NULL, NULL, NULL, 0, NOW(), 0, NOW(), 888); ")
            cursor.execute("INSERT INTO lt_org_oper(orgId, operateType, reason, reviewPerson, reviewTime, isDeleted, createdOn, createdBy, modifiedOn, modifiedBy) VALUES (" + str(orgid[0]) + ", 2, '[]', '1', NOW(), 0, NOW(), 1, NOW(), 0);")
            db.commit()
            print('修改数据库成功！！！！')
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()

    def test_revertdata(self):
        #字段还会变，先不加

        pass


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_org.py"])