import redis
import string, random


def get_activation_code(group):
    return '-'.join([''.join(random.sample(field, 4)) for i in range(group)])


def check_duplicate_code(temp_list):
    code = get_activation_code(4)
    if not temp_list.__contains__(code):
        temp_list.append(code)
        return code
    else:
        check_duplicate_code(temp_list)


pool = redis.ConnectionPool(host='60.205.218.201', port=6379, decode_responses=True)
field = string.ascii_letters + string.digits
r = redis.Redis(connection_pool=pool)
tempList = []
p = r.pipeline()
for i in range(200):
    p.lpush('code', check_duplicate_code(tempList))
p.execute()
print(r.lrange('code', 0, -1))
