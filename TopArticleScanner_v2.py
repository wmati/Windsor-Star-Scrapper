import urllib2
from bs4 import BeautifulSoup

#connect to URL, return soup object
def connect(url, headers):
    req = urllib2.Request(url, headers=headers)
    resp = urllib2.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup

#get top 6 featured links on homepage
def getLinks(url, headers):
    urls = []

    for link in connect(url, headers).find("h2", {"class": "entry-title"}):
        urls.append(link.get('href'))

    for link in connect(url, headers).find_all("h4", {"class": "entry-title"}, limit=15)[5:11]:
        urls.append(link.next_element.get('href'))

    return urls

#print get article title, text, and return formatted text
def printArticles(url, headers):
    articleTitle = connect(url, headers).find(itemprop="headline").get_text().encode('utf-8').strip()
    articleText = connect(url, headers).find(itemprop="articleBody")
    print
    return articleTitle+ \
           '\n --------------------' +\
           '\n' + articleText.get_text().encode('utf-8').strip()


url = 'http://windsorstar.com'
headers = {
    'User': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}


for site in getLinks(url, headers):
    print '{} \n {}'.format(site, printArticles(site, headers))
    print '__________________________________________________________________________________________'


