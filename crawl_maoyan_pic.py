import urllib.request
import re
import os
import requests
import HtmlCrawler


def movie_pic_crawler(url):
    htmlStr = HtmlCrawler.htmlCrawler(url)
    pic_pat = 'src="(.*?)" class="">'
    re_moviePic = re.compile(pic_pat, re.S)
    moviePicList = re_moviePic.findall(htmlStr)
    print(len(moviePicList))
    print(moviePicList)
    return moviePicList


def movie_name_crawler(url):
    htmlStr = HtmlCrawler.htmlCrawler(url)
    name_pat = 'alt="(.*?)" src="'
    re_name = re.compile(name_pat, re.S)
    nameList = re_name.findall(htmlStr)
    print(nameList)
    return nameList


# 下载十页数据  总共250张电影图片
url = "https://movie.douban.com/top250?start=0&filter="

for i in range(0, 10):
    url = "https://movie.douban.com/top250?start="+str(i*25)+"&filter="
    topath = r"\豆瓣电影海报"
    nameList = movie_name_crawler(url)
    moviePicList = movie_pic_crawler(url)
    # 将两个列表合并为字典
    movie_dic = dict(zip(nameList, moviePicList))
    # 下载电影背景图片
    for k, v in movie_dic.items():
        path = os.path.join(topath, k + ".jpg")
        r = requests.get(v)
        with open(path, "wb")as f:
            f.write(r.content)

