"""
Script to scrape Wordpress blog
"""

import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError
import re
from urllib import robotparser


def download(url, user_agent='wswp', num_retries=2, charset='utf-8', proxy=None):
    """
    Download a given URL and return the page content
    :param url: (str) URL
    :param user_agent: (str) user agent (default: wswp)
    :param num_retries: (int) number of retries if a 5xx error is seen (default: 2)
    :param charset: (str) charset if website does not include one in headers
    :param proxy: (str) proxy url, ex 'http://IP' (default: None)
    :return:
    """
    print('Downloading:', url)
    request = urllib.request.Request(url)
    request.add_header('User-agent', user_agent)
    try:
       if proxy:
           proxy_support = urllib.request.ProxyHandler({'http': proxy})
           opener = urllib.request.build_opener(proxy_support)
           urllib.request.install_opener(opener)
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


def get_robot_parser(robot_url):
    """
    Return the robots parser object using the robots_url
    """
    rp = robotparser.RobotFileParser()
    rp.set_url(robot_url)
    rp.read()
    return rp


def get_links(html):
    """
    Return a list of links from the html content
    """
    # a regular expresion to extract all links from the webpage
    webpage_regex = re._compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)

# TODO: Throttling downloads


def link_crawler(start_url, link_regex):
    """
    Crawl from the given start URL following links matches by link_regex
    :param start_url: (str) start crawler from given url website
    :param link_regex: (str) regular expression to match for links
    :return:
    """
    crawl_queue = [start_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        if html is not None:
            continue
        # filter for links matching our regular expression
        for link in get_links(html):
            if re.match(link_regex, link):
                crawl_queue.append(link)


if __name__ == '__main__':
    link_crawler('http://dudawebsite.com/blog', '/(blog)/')
