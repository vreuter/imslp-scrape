#!/usr/bin/env python
import re
from subprocess import Popen, PIPE, STDOUT


bad_links = ['http://imslp.org/wiki/Category:Arrangers',
             'http://imslp.org/wiki/Category:Composers',
             'http://imslp.org/wiki/Category:Editors',
             'http://imslp.org/wiki/Category:Librettists',
             'http://imslp.org/wiki/Category:People',
             'http://imslp.org/wiki/Category:People_by_nationality',
             'http://imslp.org/wiki/Category:Performers',
             'http://imslp.org/wiki/Category_talk:People',
             'http://imslp.org/wiki/Category:Translators',
             'http://imslp.org/wiki/Category:WIMA_files']

for url in open('people_result_page_urls.txt'):
    print("Processing: {}".format(url))
    get_links = ['lwp-request', '-o', 'links', url]
    p = Popen(get_links, shell=False, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    output = p.stdout.read()
    print("Searching/filtering output")
    links = re.findall(b'http://imslp.org/wiki/Category:.*', output)
    print("{} links".format(len(links)))
    people_pages = [x for x in links if x not in bad_links]
    print("{} people pages".format(len(people_pages)))
    for link in people_pages:
        print(link)
