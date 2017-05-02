import urllib2
from bs4 import BeautifulSoup

def getURLs(str, dict):
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find("h2", {"class": "entry-title"}):
        urls.append(link.get('href'))
    for link in soup.find_all("h4", {"class": "entry-title"}, limit=15)[5:11]:
        urls.append(link.next_element.get('href'))
    return urls

def printArticles(url, headers):
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, 'html.parser')
    articleTitle = soup.find(itemprop="headline").get_text()
    article = soup.find(itemprop="articleBody")
    print
    return articleTitle + \
           '\n --------------------' +\
           '\n' + article.get_text()




url = 'http://windsorstar.com'
headers = {
    'User': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

print getURLs(url, headers)

for site in getURLs(url, headers):
    print printArticles(site, headers)
    print '__________________________________________________________________________________________'


