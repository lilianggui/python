import xlrd, codecs, xlwt
from lxml import etree


excel = xlrd.open_workbook('excel/student.xlsx')
sheet1 = excel.sheet_by_index(0)
root = etree.Element('students')
for i in range(1, sheet1.nrows):
    stu = etree.SubElement(root, "student")
    stu.set("name", sheet1.cell(i, 0).value)
    stu.set("sex", sheet1.cell(i, 1).value)
    stu.set("age", sheet1.cell(i, 2).value)

tree = etree.ElementTree(root)
tree.write('excel/stu.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')









