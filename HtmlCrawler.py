import re
import urllib.request

def htmlCrawler(url):
    headers = {
        "Users-Agent": "Mozilla/5.0(Windows NT6.1; WOW64)AppleWebKit/537.36(KHTML,likeGecko)Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(req)

    HTML = response.read().decode("utf-8")

    pat = '<ol class="grid_view">(.*?)</ol>'
    html_pat = re.compile(pat, re.S)
    htmlStr = str(html_pat.findall(HTML))
    return htmlStr