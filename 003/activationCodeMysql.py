import string, random
import mysql.connector


def get_activation_code(group):
    return '-'.join([''.join(random.sample(field, 4)) for i in range(group)])


def check_duplicate_code(temp_list):
    code = get_activation_code(4)
    if not temp_list.__contains__(code):
        temp_list.append(code)
        return code
    else:
        check_duplicate_code(temp_list)


field = string.ascii_letters + string.digits
conn = mysql.connector.connect(user='root', password='123456', database='python_learn')
cursor = conn.cursor()
tempList = []
sql = 'insert into activation_code (code) values '
for i in range(200):
    sql += '(\'' + check_duplicate_code(tempList) + '\')'
    if i < 199:
        sql += ','
cursor.execute(sql)
cursor.close()
conn.commit()
conn.close()





