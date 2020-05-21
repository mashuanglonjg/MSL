import pytest
from page.login import Loginpage
import pymysql
import allure


@allure.feature('乐桃学院-机构申请')
class TestOrg():
    """机构申请"""
    def test_org(self, browser):
        org_page = Loginpage(browser).user_login('17777777777', 'test1234').org()
        org_page.org_apply()
        assert '审核资料已提交' == org_page.get_auditing()

    def test_del(self):
        """删除测试数据"""
        conn = pymysql.connect(host="192.168.20.80", port=61306, user="lekeAI", password="FreAv0Ed",
                               database="ltUser", charset="utf8")
        # 获取一个光标
        cursor = conn.cursor()
        # 定义将要执行的SQL语句
        sql = "delete from lt_org where name=%s;"
        name = "UI自动化机构"
        # 拼接并执行SQL语句
        cursor.execute(sql, [name])
        # 涉及写操作注意要提交
        conn.commit()
        # 关闭连接
        cursor.close()
        conn.close()

'''
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

'''
if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_org.py"])