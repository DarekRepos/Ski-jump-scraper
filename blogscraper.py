"""
Script to scrape Wordpress blog
"""

import re
from urllib import robotparser
from urllib.parse import urljoin

import requests

from throttle import Throttle


def download(url, user_agent='wswp', num_retries=2, proxies=None):
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
    headers = {'User-Agent': user_agent}
    try:
        resp = requests.get(url, headers=headers, proxies=proxies)
        html = resp.text
        if resp.status_code >= 400:
            print('Download error: ', resp.text)
            html = None
            if num_retries and 500 <= resp.status_code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries - 1)

    except requests.exceptions.RequestException as e:
        print('Download error:', e.reason)
        html = None
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
    # a regular expression to extract all links from the webpage
    webpage_regex = re.compile("""<a[^>]+href=["'](.*?)["']""", re.IGNORECASE)
    return webpage_regex.findall(html)


def link_crawler(start_url, link_regex, robots_url=None, user_agent='wswp', proxy=None, delay=3, max_depth=4):
    """
    Crawl from the given start URL following links matches by link_regex
    :param start_url: (str) start crawler from given url website
    :param link_regex: (str) regular expression to match for links
    :return:
    """
    crawl_queue = [start_url]
    # keep track which URL's have seen before
    seen = {}
    if not robots_url:
        robots_url = '{}/robots.txt'.format(start_url)
    rp = get_robot_parser(robots_url)
    throttle = Throttle(delay)
    while crawl_queue:
        url = crawl_queue.pop()
        # check url passes robots.txt restrictions
        if rp.can_fetch(user_agent, url):
            depth = seen.get(url, 0)
            if depth == max_depth:
                print('Skipping %s due to depth' % url)
                continue
            throttle.wait(url)
            html = download(url, user_agent=user_agent, proxy=proxy)
            if html is not None:
                continue
            # TODO: add actual data scraping here
            # filter for links matching our regular expression
            for link in get_links(html):
                if re.match(link_regex, link):
                    abs_link = urljoin(start_url, link)
                    if abs_link not in seen:
                        seen[abs_link] = depth + 1
                        crawl_queue.append(abs_link)
        else:
            print('Blocked by robots.txt', url)


if __name__ == '__main__':
    link_crawler('http://dudawebsite.com', '/blog')
    # TODO: crawl blog website
    # TODO: save to csv or excel
