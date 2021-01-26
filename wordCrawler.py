#!/usr/bin/python3
# PYTHON_ARGCOMPLETE_OK

from urllib.request import urljoin
import requests
from bs4 import BeautifulSoup
import argparse
import argcomplete
import sys
import ssl
import re
import urllib3
import pyfiglet

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Color:
    RED='\x1b[91m'
    YELLOW='\x1b[33m'
    GREEN='\x1b[92m'
    RESET='\x1b[0m'

class WebSpider(object):
    def __init__(self, depth, urls):
        self.visited = []
        self.unreachable = []
        self.discovered = ()
        self.urls = urls
        self.depth = depth + 1  

    def __getLinks(self, html, url):
        soup = BeautifulSoup(html.text, "html.parser")
        myset = set()
        for link in soup.find_all("a"):
            myset.add(urljoin(url, link.get("href")).strip("/").split("#")[0])
        return myset

    def __sortDiscoveredLinks(self):
        new_links = [link for link in self.discovered if not link in self.visited]
        with open("discovered.txt", "a+") as log_file:
            log_file.writelines("\n".join(new_links))
        self.urls = new_links
        self.discovered = () # Flush

    def __do(self, args, url, html):
        try:
            keywords = open(args.wordlist,'rt').read().splitlines()
            for keyword in keywords:
                if re.search(keyword, html.text, re.IGNORECASE):
                    print(f"{Color.GREEN}keyword {Color.YELLOW}{keyword}{Color.GREEN} found!!!{Color.RESET}")
                    print(f"{Color.GREEN}url -> {Color.YELLOW}{url}{Color.RESET}\n\n")

                    with open(args.outputFile,'a+') as m:
                        m.write(url + " -> " + "(" + keyword + ")\n")
        except Exception as e:
            print(e)

    def crawl(self, args, urls=[]):
        self.urls.extend(urls)
        for url in self.urls:
            print(f"{Color.GREEN}Crawling {url}...{Color.RESET}")
            try:
                headers = {'User-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
                try:
                    html = requests.get(url, headers=headers)
                except Exception as e:
                    print(e)
                self.visited.append(url)
                self.__do(args, url, html)
                self.discovered = self.__getLinks(html, url)
                self.__sortDiscoveredLinks()
            except ValueError:
                print(f"{Color.RED}Malformed URL ({Color.YELLOW}{url}){Color.RESET}")
            except:
                print(f"{Color.RED}Could not open {Color.YELLOW}{url}{Color.RESET}")
                self.unreachable.append(url)
        if self.depth == 1:
            pass
        else:
            self.depth = self.depth - 1
            self.crawl(args, urls)


def parse_args():
    parser = argparse.ArgumentParser(description='crawler for a website to find keywords')
    url = parser.add_mutually_exclusive_group()
    url.add_argument('-u', '--url', help='specify the url to crawl')
    url.add_argument('-r', '--readFile', help='specify a file with urls to crawl')
    parser.add_argument('-d', '--depth', type=int, help='depth for crawl', default=1)
    parser.add_argument('-w', '--wordlist', help='path for wordlist with keywords to search for', default='wordlist.txt')
    parser.add_argument('-o', '--outputFile', help='path to output file', default='output.txt')

    argcomplete.autocomplete(parser)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    return parser.parse_args()

def main():
    ascii_banner = pyfiglet.figlet_format("wordCrawler")
    print(f"{Color.GREEN}{ascii_banner}{Color.RESET}")
    print(f"{Color.RED}\t\t\t\t\t\t\tby MrCalv1n{Color.RESET}\n")

    args = parse_args()

    if args.readFile != None:
        urls = open(args.readFile).read().splitlines()
    elif args.url != None:
        urls = args.url
        urls = urls.split(',')
    else:
        print("please specify an url or a read file with urls\n")
        parser.print_help(sys.stderr)
        sys.exit(1)

    spider = WebSpider(args.depth, urls)
    spider.crawl(args)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print(f'{Color.RED}[*] cancelled...{Color.RESET}')

