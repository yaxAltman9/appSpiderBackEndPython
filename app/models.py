pip install flask-mysqldb

import logging


class JobModel:
    def __init__(self, mysql: MySQL):
        self.mysql = mysql

    def get_all_jobs(self, search_term, offset, limit):
        cur = self.mysql.connection.cursor()
        query = """
            SELECT * FROM job 
            WHERE name LIKE %s OR area LIKE %s OR taglist LIKE %s OR salary LIKE %s 
            OR link LIKE %s OR company LIKE %s OR `desc` LIKE %s
            LIMIT %s, %s
        """
        params = ['%' + search_term + '%'] * 7 + [offset, limit]

        logging.info('执行查询: ' + query)
        logging.info('参数: ' + str(params))

        cur.execute(query, params)
        results = cur.fetchall()
        cur.close()
        return results

    def check_connection(self):
        try:
            cur = self.mysql.connection.cursor()
            cur.execute("SELECT 1")
            cur.close()
            return True
        except Exception as e:
            logging.error('检查数据库连接时出错:', e)
            return False
