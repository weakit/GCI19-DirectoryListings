import requests as r
import time
import re

SITE = "http://tkgeisel.com/pics/"
ROOT = re.search(r'^((?:https?:\/\/)?(?:[^@\/\n]+@)?(?:www\.)?[^:\/\n]+)', SITE)[0]
CHECK_LINKS = False


directories = set()


def get_source():
    request = r.get(SITE)
    if request.status_code != 200:
        print("Can't reach ", SITE)
        exit(-1)
    return request.text[request.text.index('\n'):]


def get_urls(s):
    return re.findall(r'"([^"<>=]*\/[^"<>=]*)"', s)


def parse_url(s):
    a = [x + '/' for x in s.split('/')[:-1] if not re.findall('[:;&]', x)]
    for x in range(1, len(a) + 1):
        path = ''.join(a[:x])
        directories.add((ROOT if path.startswith('/') else SITE) + path)


def check_dirs():
    for x in directories.copy():
        if r.get(x).status_code not in [403, 200]:
            directories.remove(x)


if __name__ == '__main__':
    print('Getting webpage', end='', flush=True)
    source = get_source()
    print('. Done.\nScraping links', end='', flush=True)
    for url in get_urls(source):
        parse_url(url)
    if CHECK_LINKS:
        print('. Done.\nChecking links', end='', flush=True)
        check_dirs()
    print(". Done.\n\nDirectories:")
    for directory in directories:
        print(directory)
