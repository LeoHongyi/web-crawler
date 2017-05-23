# -*- coding: utf-8 -*-
__author__ = 'hongyi'
import hashlib
import re
import MySQLdb

def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def extract_num(text):
    #从字符串中提取出数字
    match_re = re.match(".*?(\d+).*", text)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums
def test():
    conn = MySQLdb.connect('localhost','root','root','article_spider', charset="utf8", use_unicode=True)
    if conn:
        print("successful")
        cursor = conn.cursor()
        insert_sql = """
                    insert into jobbole_article(title,create_date ,url , fav_nums)
                    VALUES (%s, %s, %s, %s)
                """
        cursor.execute(insert_sql, ("title", "1992-01-02", "google.com", 1))
        print(insert_sql)
        conn.commit()


if __name__ == "__main__":
    print (get_md5("http://jobbole.com".encode("utf-8")))
    test()