# _*_ coding:utf-8 _*_
import urllib.request
import urllib.error

req = urllib.request.Request("http://blog.csdn.net/ded")
try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.reason)