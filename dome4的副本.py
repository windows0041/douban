import requests    # 导入requests模块
import re          # 导入re模块
for i in range(0, 11):    # 完善URL的参数 并设置循环
    new_url = f"https://movie.douban.com/top250?start={i}&filter="
    url = new_url
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }
    test = requests.get(url=url, headers=head)
    test.encoding = 'utf-8'   # enconfing 设置编码格式
    obj = re.compile(r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<br>(?P<year>.*?)&nbsp;.*?<span class="rating_num" property="v:average">(?P<grade>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)
    result = obj.finditer(test.text)   # finditer 查找所有匹配内容
    for item in result:
        dic = item.groupdict()  # groupdict 返回一个包含所有匹配到的命名组的组名为键值和命名
        dic['year'] = dic['year'].strip()    # strip 去除换行符和空格
#    print(type(dic))
        with open('豆瓣.txt', mode='a', encoding= 'utf-8') as f:  # open打开或新建一个文件 '豆瓣.txt'文件名 mode写入方式为追加'a'
            f.write(str(dic))    # f.write 把dic转换成str并写入到新建的豆瓣.txt文件中
    print('over!!!')