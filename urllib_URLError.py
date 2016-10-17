# _*_ coding:utf-8 _*_
#引入 urllib.request 和 urllib.error两个模块
import urllib.request
import urllib.error
req = urllib.request.Request("http://www.xxxxxx.com")
try:
	resonpose = urllib.request.urlopen(req)
except urllib.error.URLError as e:
	print (e.reason)