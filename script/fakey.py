#!/usr/bin/env python3
import requests
import json
import re
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

class FAKey:
    def __init__(self, args):
        self.path = open('./config/path_config.txt').read().split()
        self.lregex = open('./config/regexs_key.json').read()
        self.target = args.t
        self.workers = 5
        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36'}
        self.session = requests.Session()

    def scanning(self):
        def check_key(path):
            regex = json.loads(self.lregex)
            response = self.session.get(url=self.target + path, headers=self.headers, allow_redirects=True, timeout=3)
            for n,p in regex.items():
                found = re.search(p, response.text)
                if found:
                    print(self.target + path + ' Found [ ' + n + ' ]')
                    open('key-found.txt', '+a').write(self.target + path + ' [ ' + n + ' ]' +'\n')
                    return
                else:
                    print(self.target + path + ' Not found [ ' + n + ' ]')

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            try:
                for result in executor.map(check_key, self.path):
                    pass
            except futures._base.TimeoutError:
                print('[!] TIMEOUT')
