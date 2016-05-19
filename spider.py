#encoding=utf-8
import urllib
from bs4 import BeautifulSoup


html=urllib.urlopen("http://www.wooyun.org/corps/page/44")
bsobj=BeautifulSoup(html.read())
print (bsobj.h1)
