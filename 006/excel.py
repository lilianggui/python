import xlrd, codecs, xlwt
from lxml import etree


tree = etree.parse('excel/student.xml')
root = tree.getroot()

excel = xlwt.Workbook()
base = excel.add_sheet('学生信息')
base.write(0, 0, '姓名')
base.write(0, 1, '性别')
base.write(0, 2, '年龄')
for i in range(1, len(root)+1):
    article = root[i-1]
    base.write(i, 0, article.get('name'))
    base.write(i, 1, article.get('sex'))
    base.write(i, 2, article.get('age'))
excel.save('excel/student.xlsx')

