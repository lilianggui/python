import string, random

field = string.ascii_letters + string.digits


def get_activation_code(group):
    return '-'.join([''.join(random.sample(field, 4)) for i in range(group)])


def check_duplicate_code(temp_list):
    code = get_activation_code(4)
    if not temp_list.__contains__(code):
        temp_list.append(code)
        return code
    else:
        check_duplicate_code(temp_list)


with (open(r'C:\Users\Lange\Desktop\python\002\result.txt', 'w')) as f:
    tempList = []
    for i in range(200):
        f.write(check_duplicate_code(tempList)+'\n')

print('finished!')

