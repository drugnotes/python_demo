# _*_ coding:utf-8 _*_
import urllib.request   #引入 urllib.request，Python3 之后将 urllib2 改为 urllib.request
import urllib.parse     #引入 urllib.parse，用户数据处理模块

url = "http://wiki.jikexueyuan.com/list/python"

#命名数据类型
values = {
            'username':'jike_6049765',
            'password':'xxxxxxxx'
        }
#定义 header 等头部信心
headers={
        'Referer':'http://www.jikexueyuan.com/Upgrade-Insecure-Requests:1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

#通过urlencode()的方法处理'用户数据
data = urllib.parse.urlencode(values).encode('utf-8')
req = urllib.request.Request(url,data,headers)
response = urllib.request.urlopen(url)
page = response.read().decode('utf-8')
print (page)
