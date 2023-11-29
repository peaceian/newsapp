from django.shortcuts import render
from bs4 import BeautifulSoup
import re
import urllib
import requests
import random
import pandas as pd
# Create your views here.

def News(request):
    url = 'https://news.pts.org.tw/dailynews'
    #url = f'https://news.pts.org.tw/search/%E5%88%97%E8%A1%A8'

#自訂標頭  
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
 "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
 "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
 "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
 "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
 "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
 "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
 "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
 "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
 "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
 "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
    headers = {'user-agent': random.choice(user_agents)} #偽裝使用者
#header代入網址
    data = requests.get(url=url, headers=headers)
    print(data)
    
    #data_res = urllib.request.Request(url=url,headers=headers)
    #data = urllib.request.urlopen(data_res)
    #data = data.read().decode('utf-8')  
    #sp = BeautifulSoup(data, "html.parser")
    sp = BeautifulSoup(data.text,'html.parser')
    #print(sp.title)
    #print(sp.figure)
    #print(sp.find_all('a',string='article'))
    #print(sp.select('div',{"class":"embed-responsive embed-responsive-16by9"})[0].get('href'))
    #print(sp.find('img',{"class":"cover-fit"}))
    #print(sp.find_parent('time'))
    #print(sp.find_parent('h2'))
    #print(sp.find('div',{"class":"news-info"}))
    #print(sp.find_all("a",href = re.compile('article')))
    #print(sp.find_all('li'))
    #print(sp.find_all('h2'))
    


    #當日日期
    #date = sp.find("div",{"class" : "break-news-time"})
    #print(date.text)

    #每筆資料
    time = []
    times = sp.find_all('time')
    for time1 in times:
        time.append(time1.text)
        print(time1.text)

    #圖片
    #img = []
    #imgs = sp.find_all('img',{"class":"cover-fit"},src=re.compile('mrdia'))
    #for img1 in imgs:
    #    img.append(img1['src'])
        #print()

    #標題
    title = []
    titles = sp.find_all('a',href = re.compile('/article'))
    for title1 in titles:
        title.append(title1.text)
        print(title1.text)

    #網址
    link = []
    
    links = sp.find_all("a",href = re.compile('/article'))
    #links = h2.find_all('a')
    #links = a.find_all("a",href = re.compile('article'))#找出a href 中有'article'字詞的a
    
    print(links)
    
    #links = list(set(links))#pts.org 中，<a>沒有標籤，同網址出現兩次，用set消除
    
    for link1 in links:
        link.append(link1['href'])
    
    all = zip(time,title,link)
    
    return render(request,'base.html',locals())

def Newslist(request):
    url = f'https://news.pts.org.tw/dailynews/'
    user_agents = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        ]
    headers = {'user-agent': random.choice(user_agents)} #偽裝使用者
    data = requests.get(url, headers=headers)
    print(data)
    soup = BeautifulSoup(data.text,'html.parser')
    elem = soup.select('article')
    #title = e.select('a')
    #date = e.select('time')
    #link = e.select('a').get('href')
    #cate = e.select('.news-info').get('a')

    title_list = []
    date_list = []
    link_list = []
    #cate_list = []

    for e in elem:
        title_list = [title.text for title in e.find_all('a',href=re.compile('/article'))]#比對網址用正則表達式
        #print(title_list)
        link_list = [i.get('href') for i in e.find_all('a',href=re.compile('/article'))]
        #print(link_list)
        date_list = [date.string for date in e.find_all("time")]
        #print(date_list)
        #cate_list = [cate.text for cate in e.find_all('a',href=re.compile('/category'))]

    #如果你不清楚這個運算方式，
    # title_list = [title.text for title in e.select("a")]
    # 你可以把它看成是這樣：
    # for title in e.select("a"):
        # title_list.append(title.text)

    #df = pd.DataFrame()
    #df["title"]=title_list
    #df["category"]= cate_list
    #df["date"]=date_list
    #df["link"]=link_list

    print(title_list)
    print(link_list)
    print(date_list)
    #print(cate_list)

    all = zip(date_list,title_list,link_list)

    return render(request,'base2.html',locals())