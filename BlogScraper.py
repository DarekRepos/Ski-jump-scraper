"""
Script to scrape Wordpress blog
"""

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re

def download(url, user_agent='wswp', num_retries=2, charset='utf-8'):
   print('Downloading:', url)
   request = urllib.request.Request(url)
   request.add_header('User-agent',user_agent)
   try:
      resp = urllib.request.urlopen(request)
      cs = resp.headers.get_content_charset()
      if not cs:
         cs = charset
      html = resp.read().decode(cs)
   except (URLError, HTTPError, ContentTooShortError) as e:
      print('Download error:', e.reason)
      html = None
      if num_retries > 0:
          if hasattr(e, 'code') and 500 <= e.code < 600:
              return download(url, num_retries - 1)
   return html

def crawl_sitemap(url):
   sitemap = download(url)
   links = re.findall('<loc>(.*?)</loc>', sitemap)
   for link in links:
      html = download(link)


if __name__ == '__main__':
   crawl_sitemap('https://dudawebsite.com')