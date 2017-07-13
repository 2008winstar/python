import urllib.request
print(urllib.request.urlopen('http://quan.qq.com').read().decode('utf-8'))
