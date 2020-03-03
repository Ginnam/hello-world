import requests
import os

#要爬取的链接
url = 'http://n.sinaimg.cn/photo/transform/700/w1000h500/20200303/cca3-iqfqmat7471844.jpg'

#文件保存目录
root = 'D://Download//'

#文件保存路径(自动填写）
path = root + url.split('/')[-1]

try:
    r = requests.get(url)
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(r.content)
        print('文件保存成功！')
    else:
        print('文件已存在！')
except:
    print('发生了未知错误，请重新尝试！')