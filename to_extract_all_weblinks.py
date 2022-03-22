#This is a program to extract all weblinks in python 

""" we are using requests module of python 
    It allows us to send HTTP requests.
    These HTTP requests returns a responce object with all response data"""

""" urllib is another package which is used, it allows to open and read urls"""
"""beautifulsoup is a library which is used to scrap data from website"""

import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import colorama

#initializing the colorama module
colorama.init()

GREEN = colorama.Fore.GREEN
RESET = colorama.Fore.RESET


def is_valid(url):

    # To checks whether `url` is a valid URL.

    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)



def get_all_website_links(url):

    #Returns all URLs that is found on `url` in which it belongs to the same website
    
    # all URLs of `url`
    urls = set() # to avoid redundancy we used sets
    
    domain_name = urlparse(url).netloc      # domain name of the URL without the protocol
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
     #html parser is a converter which converts data into html form
     
    
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            # for empty link code  will continue
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        if not is_valid(href):
            # not a valid URL
            continue
        if href in urls:
            # already in the set
            continue
        print(f"{GREEN}[*] Link: {href}{RESET}")
        urls.add(href)
    return urls


if __name__ == "__main__":
    url = input("[+] Enter any URL : ")
    get_all_website_links(url)