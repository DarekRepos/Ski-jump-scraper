# _*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup

url = 'http://http://www.skokinarciarskie.pl/'
ss = requests.Session()
res = ss.get(url)
soup = BeautifulSoup(res.content, 'html5lib')

# locate the area row
tr = soup.find(attrs={'class': 'program_czas'})
area = tr.text  # extract the data
print(area)
