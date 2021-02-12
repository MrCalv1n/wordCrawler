[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)](https://pypi.python.org/pypi/yt2mp3/)


wordCrawler
=============

Tool to crawl websites and check if certain keywords are present in their content.

Example usage
-----

**To use it as a command-line script:**

Single site to crawl
```bash
     python3 wordCrawler.py -u "https://www.google.com/" -w wordlist.txt -o outputfile.txt
```     
Multiple sites to crawl
```bash
     python3 wordCrawler.py -u "https://www.google.com/,https://www.microsoft.com/" -w wordlist.txt -o outputfile.txt
```
Input file with websites to crawl
```bash
     python3 wordCrawler.py -r FileWithSites.txt -w wordlist.txt -o outputfile.txt
```

**Command Options:**

```bash 
                          _  ____                    _           
__      _____  _ __ __| |/ ___|_ __ __ ___      _| | ___ _ __ 
\ \ /\ / / _ \| '__/ _` | |   | '__/ _` \ \ /\ / / |/ _ \ '__|
 \ V  V / (_) | | | (_| | |___| | | (_| |\ V  V /| |  __/ |   
  \_/\_/ \___/|_|  \__,_|\____|_|  \__,_| \_/\_/ |_|\___|_|   
                                                              

						by MrCalv1n

usage: wordCrawler.py [-h] [-u URL | -r READFILE] [-d DEPTH] [-w WORDLIST]
                      [-o OUTPUTFILE]

crawler for a website to find keywords

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     specify the urls to crawl separated by commas
  -r READFILE, --readFile READFILE
                        specify a file with urls to crawl
  -d DEPTH, --depth DEPTH
                        depth for crawl
  -w WORDLIST, --wordlist WORDLIST
                        path for wordlist with keywords to search for
  -o OUTPUTFILE, --outputFile OUTPUTFILE
                        path to output file

```

Installation
------------
```bash
git clone https://github.com/MrCalv1n/wordCrawler.git
cd wordCrawler/
pip3 install -r requirements.txt
```
