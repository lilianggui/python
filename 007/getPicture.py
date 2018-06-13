#coding = utf-8
import urllib
import urllib.request
import re
import os


def get_html(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def get_img(html, page_num):
    html = html.decode('utf-8')
    reg = 'src="(.+?\.jpg)" alt='
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        target_path = 'picture\\%s' % page_num
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        urllib.request.urlretrieve(imgurl, 'picture\\%s\\%s.jpg' % (page_num, x))
        x += 1
    return imglist


def get_next_page_url(html):
    html = html.decode('utf-8')
    reg = '="next" href="(.+?\.html)">下一页'
    next_page = re.compile(reg)
    next_page_list = re.findall(next_page, html)
    if next_page_list:
        return next_page_list[0]


def loop_get_img(url, web_add, page_num):
    print('正在获取第' + str(page_num) + '页的图片...')
    full_url = web_address + url
    try:
        html = get_html(full_url)
        get_img(html, page_num)
    except Exception as err:
        print(err)
    next_page_url = get_next_page_url(html)
    if next_page_url:
        loop_get_img(next_page_url, web_add, page_num+1)


web_address = 'http://pic.yxdown.com'
first_page_url = "/list/0_0_1.html"
loop_get_img(first_page_url, web_address, 1)

