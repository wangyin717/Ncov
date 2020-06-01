#-*- coding = utf-8 -*-
#@Time : 2020/3/26 20:13
#@Author : WangYin
#@File : spider.py
#@Software : PyCharm
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl = "https://ncov.dxy.cn/ncovh5/view/pneumonia"
    #1.爬取网页
    getData(baseurl)



    #2.解析数据
    #3.保存数据
    # saveData(savepath)



findlink = re.compile(r'<a href="(.*?)">')      #创建正则表达式规则
findImage = re.compile(r'<img.*src="(.*?)"',re.S)   #影片图片的链接 re.S让换行符包含在字符中
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findIng = re.compile(r'<span> class="inq">(.*)</span>')
findDetails = re.compile(r'<p class="">(.*)</p>',re.S)

#爬取网页
def getData(baseurl):
    datalist = []
    html = askURL(url)        #保存获取到的网页源码

        #逐一解析数据
    soup = BeautifulSoup(html,"html.parser")
    for item in soup.find_all("div",class_="areaBox___Sl7gp themeA___1BO7o numFormat___nZ7U7"):          #查找符合要求的字符串，形成列表
        data = []        #保存一部电影的所有信息
        item = str(item)
        print(item)
        #break
        #link = re.findall(findDetails,item)[0]   #re库用来查找指定字符串
        #print(link)



    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    #用户代理 表示告诉服务器我们是什么类型的浏览器
    #模拟浏览器头部信息
    head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e,reason)
    return html



#保存数据
# def saveData(savepath):
#     print()

if __name__ == "__main__":
    main()








