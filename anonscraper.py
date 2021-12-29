#!/usr/bin/python3
"""
   ______________             __
  |__  /__  / __ \_________  / /______ ______
   /_ <  / / / / / ___/ __ \/ //_/ __ `/ ___/
 ___/ / / / /_/ / /  / /_/ / ,< / /_/ (__  )
/____/ /_/\____/_/   \____/_/|_|\__,_/____/

AnonScraper

Scrapes uploaded files to AnonFile by provided query using Google Dorking

Author: 370rokas <https://github.com/370rokas/>
Created: 29th December, 2021
"""

from colorama import Fore
import requests
import getopt
import sys
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
}


def google(q):
    s = requests.Session()
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?&q=site%3Aanonfile.com+' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers)

    output = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', r.text)

    return output


def main():
    print(Fore.MAGENTA + '''
       ______________             __
      |__  /__  / __ \_________  / /______ ______
       /_ <  / / / / / ___/ __ \/ //_/ __ `/ ___/
     ___/ / / / /_/ / /  / /_/ / ,< / /_/ (__  )
    /____/ /_/\____/_/   \____/_/|_|\__,_/____/
    
    AnonScraper
    Author: 370rokas <https://github.com/370rokas/anonscraper>
        ''' + Fore.RESET)

    argv = sys.argv[1:]
    options = "hq:f:"
    l_options = ["help", "query", "filename"]

    query = ""
    filename = ""

    def display_help():
        print(Fore.WHITE + "anonscraper.py -q <query> -f <filename>" + Fore.RESET)
        sys.exit()

    try:
        args, vals = getopt.getopt(argv, options, l_options)

        if len(args) == 0:
            display_help()

        for c_arg, c_val in args:
            if c_arg in ('-h', '--help'):
                display_help()

            if c_arg in ('-q', '--query'):
                query = c_val

            if c_arg in ('-f', '--filename'):
                filename = c_val

    except getopt.error as err:
        print(str(err))

    urls = google(query)
    filtered = []

    for url in urls:
        if ("anonfile.com/" in url and url != "https://anonfile.com" and not "google." in url):
            filtered.append(url)

    for i in range(len(filtered)):
        print(Fore.CYAN + str(i+1) + ". " + filtered[i] + Fore.RESET)
        if filename != "":
            open(filename, 'a').write(filtered[i] + "\n")

    if filename != "":
        print(Fore.GREEN + "[i] Saved results into " + filename)
    print(Fore.MAGENTA + "[i] Finished. Got " + str(len(filtered)) + " results." + Fore.RESET)


if __name__ == '__main__':
    main()
