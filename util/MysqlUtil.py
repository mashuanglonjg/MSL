import pymysql as mysql
# 引入python中的traceback模块，跟踪错误
import traceback
# 引入sys模块
import sys

class MysqlUtil():
    #获取数据库的连接
    def getConnect(self):
        # 参数依次是：IP地址,数据库登录名，端口号，数据库密码，数据库实体名称,指定字符集 （未指定可能出现中文乱码）
        db = mysql.connect(host = "192.168.20.80",port = 61306,user = "lekeAI",password = "FreAv0Ed",db = "ltUser", charset = "utf8")
        return db

    #查询数据库：单个结果集
    #fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    def fetchone(self, sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            result = cursor.fetchone()
        except:  # 方法二：采用traceback模块查看异常
            # 输出异常信息
            traceback.print_exc()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return result

    #查询数据库：多个结果集
    #fetchall(): 接收全部的返回结果行.
    def fetchall(self, sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            results = cursor.fetchall()
        except:  # 方法三：采用sys模块回溯最后的异常
            # 输出异常信息
            info = sys.exc_info()
            print(info[0], ":", info[1])
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()
        return results

    #插入数据
    def insert(self, sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()

    #删除结果集
    def delete(self, sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()
        except:  # 如果你还想把这些异常保存到一个日志文件中，来分析这些异常
            # 将错误日志输入到目录文件中
            f = open("c:log.txt", 'a')
            traceback.print_exc(file=f)
            f.flush()
            f.close()
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()

    #更新结果集
    def update(self, sql):
        # 获取数据库连接
        db = self.getConnect()
        # 使用cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql)
            db.commit()
        except:
            # 如果发生异常，则回滚
            db.rollback()
        finally:
            # 最终关闭数据库连接
            db.close()