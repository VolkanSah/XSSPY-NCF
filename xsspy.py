#!/usr/bin/env python3
import mechanize
import sys
import http.client as httplib
import argparse
import logging
from urllib.parse import urlparse

# Funktion zum Einlesen der Payloads aus einer Datei
def read_payloads_from_file(file_path):
    with open(file_path, 'r') as file:
        payloads = [line.strip() for line in file]
    return payloads

br = mechanize.Browser()  # initiating the browser
br.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
]
br.set_handle_robots(False)
br.set_handle_refresh(False)

# inline payloads
# payloads = ['<svg onload=alert(1)>', '" onfocus="alert(1);', 'javascript:alert(1)']
# payloads from file
payload_file_path = 'payloads.txt'
payloads = read_payloads_from_file(payload_file_path)

blacklist = ['.png', '.jpg', '.jpeg', '.mp3', '.mp4', '.avi', '.gif', '.svg', '.pdf']
xssLinks = []  # TOTAL CROSS SITE SCRIPTING FINDINGS

class color:
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @staticmethod
    def log(lvl, col, msg):
        logger.log(lvl, col + msg + color.END)


print(color.BOLD + color.RED + """
 __  __        ____           ___   _  ____ _______  
 \ \/ /___ ___|  _ \ _   _   / / \ | |/ ___|  ___\ \ 
  \  // __/ __| |_) | | | | | ||  \| | |   | |_   | |
  /  \\__ \__ \  __/| |_| | | || |\  | |___|  _|  | |
 /_/\_\___/___/_|    \__, | | ||_| \_|\____|_|    | |
                     |___/   \_\                 /_/ 

XssPy NCF - Simplifying XSS Detection
Created by Nemesis Cyber Force (NCF)
© S. Volkan Kücükbudak / Mr.Chess

XssPy (NCF) is designed for security researchers and ethical hackers to identify XSS vulnerabilities 
in web applications. It automates the testing process by analyzing web pages and submitting payloads 
to detect security issues.
For stable and nightly versions, visit: https://github.com/VolkanSah/XSSPY-NCF/

Note: This tool is for ethical hacking only. Unauthorized use may result in legal consequences. 
Always seek permission before testing any web application.
""" + color.END)

logger = logging.getLogger(__name__)
lh = logging.StreamHandler()  # Handler for the logger
logger.addHandler(lh)
formatter = logging.Formatter('[%(asctime)s] %(message)s', datefmt='%H:%M:%S')
lh.setFormatter(formatter)

parser = argparse.ArgumentParser()
parser.add_argument('-u', action='store', dest='url', help='The URL to analyze')
parser.add_argument('-e', action='store_true', dest='compOn', help='Enable comprehensive scan')
parser.add_argument('-v', action='store_true', dest='verbose', help='Enable verbose logging')
parser.add_argument('-c', action='store', dest='cookies', help='Space separated list of cookies', nargs='+', default=[])
# parser.add_argument('-i', action='store_true', dest='poisonivory', help='Use PoisonIvory Nemesis ')
results = parser.parse_args()

logger.setLevel(logging.DEBUG if results.verbose else logging.INFO)

def testPayload(payload, p, link):
    br.form[str(p.name)] = payload
    br.submit()
    # if payload is found in response, we have XSS
    if payload in br.response().read():
        color.log(logging.DEBUG, color.BOLD + color.GREEN, 'XSS found!')
        report = f'Link: {link}, Payload: {payload}, Element: {p.name}'
        color.log(logging.INFO, color.BOLD + color.GREEN, report)
        xssLinks.append(report)
    br.back()

def initializeAndFind():
    if not results.url:  # if the url has been passed or not
        color.log(logging.INFO, color.GREEN, 'Url not provided correctly')
        return []

    firstDomains = []  # list of domains
    allURLS = [results.url]  # just one url at the moment
    largeNumberOfUrls = []  # in case one wants to do comprehensive search

    # doing a short traversal if no command line argument is being passed
    color.log(logging.INFO, color.GREEN, 'Doing a short traversal.')
    for url in allURLS:
        smallurl = str(url)
        # Test HTTPS/HTTP compatibility. Prefers HTTPS but defaults to
        # HTTP if any errors are encountered
        try:
            test = httplib.HTTPSConnection(smallurl)
            test.request("GET", "/")
            response = test.getresponse()
            if response.status in [200, 302]:
                url = "https://www." + str(url)
            elif response.status == 301:
                loc = response.getheader('Location')
                url = loc.scheme + '://' + loc.netloc
            else:
                url = "http://www." + str(url)
        except:
            url = "http://www." + str(url)
        try:
            br.open(url)
            for cookie in results.cookies:
                color.log(logging.INFO, color.BLUE, f'Adding cookie: {cookie}')
                br.set_cookie(cookie)
            br.open(url)
            color.log(logging.INFO, color.GREEN, f'Finding all the links of the website {url}')
            for link in br.links():        # finding the links of the website
                if smallurl in str(link.absolute_url):
                    firstDomains.append(str(link.absolute_url))
            firstDomains = list(set(firstDomains))
        except:
            pass
        color.log(logging.INFO, color.GREEN, f'Number of links to test are: {len(firstDomains)}')
        if results.compOn:
            color.log(logging.INFO, color.GREEN, 'Doing a comprehensive traversal. This may take a while')
            for link in firstDomains:
                try:
                    br.open(link)
                    # going deeper into each link and finding its links
                    for newlink in br.links():
                        if smallurl in str(newlink.absolute_url):
                            largeNumberOfUrls.append(newlink.absolute_url)
                except:
                    pass
            firstDomains = list(set(firstDomains + largeNumberOfUrls))
            color.log(logging.INFO, color.GREEN, f'Total Number of links to test have become: {len(firstDomains)}')
    return firstDomains

def findxss(firstDomains):
    # starting finding XSS
    color.log(logging.INFO, color.GREEN, 'Started finding XSS')
    if firstDomains:    # if there is at least one link
        for link in firstDomains:
            blacklisted = False
            y = str(link)
            color.log(logging.DEBUG, color.YELLOW, str(link))
            for ext in blacklist:
                if ext in y:
                    color.log(logging.DEBUG, color.RED, '\tNot a good url to test')
                    blacklisted = True
                    break
            if not blacklisted:
                try:
                    br.open(str(link))    # open the link
                    if br.forms():        # if a form exists, submit it
                        params = list(br.forms())[0]    # our form
                        br.select_form(nr=0)    # submit the first form
                        for p in params.controls:
                            par = str(p)
                            # submit only those forms which require text
                            if 'TextControl' in par:
                                color.log(logging.DEBUG, color.YELLOW, f'\tParam: {p.name}')
                                for item in payloads:
                                    testPayload(item, p, link)
                except:
                    pass
        color.log(logging.DEBUG, color.GREEN + color.BOLD, 'The following links are vulnerable: ')
        for link in xssLinks:        # print all xss findings
            color.log(logging.DEBUG, color.GREEN, '\t' + link)
    else:
        color.log(logging.INFO, color.RED + color.BOLD, '\tNo link found, exiting')

# calling the function
firstDomains = initializeAndFind()
findxss(firstDomains)
