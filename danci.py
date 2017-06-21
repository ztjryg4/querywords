# -*- coding: utf-8 -*-  
import urllib.request
import re
iPos = 0

n = int(input("请输入单词数："))

for dancicnt in range(0,n):
 
 danci = input("请输入单词:")

 def getHtml(url):
     page = urllib.request.urlopen(url)
     html = page.read()
     return html

 wangzhi="http://dict.youdao.com/app/baidu/search?q="+danci

 html = getHtml(wangzhi)

 def getImg(html):
     html = html.decode('utf-8')
     reg = r'<li>(.*?)</li>'
     imgre = re.compile(reg)
     imglist = re.findall(imgre,html)
     for i in range(0,len(imglist)):
      yuansu = ''.join(imglist[i])
      chazhao = '. '
      nPos = yuansu.find(chazhao)
      if nPos >= 0:
       iPos = i
     result = ''
     for c in range(0,iPos+1):
      if c == 0:
       s = ''
      else:
       s = '\n'
      result = result + s + ''.join(imglist[c])
     return result

 print(getImg(html))
