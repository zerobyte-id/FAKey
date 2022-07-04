#!/usr/bin/env python3
import argparse
from script.fakey import FAKey
def argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', metavar='example.com', type=str, help='target', required=True)
    args = parser.parse_args()
    return args

def main():
    print('''---------------------------------------\n(     _____ _    _  __                )\n(     |  ___/ \  | |/ /___ _   _      )\n(     | |_ / _ \ | ' // _ \ | | |     )\n(     |  _/ ___ \| . \  __/ |_| |     )\n(     |_|/_/   \_\_|\_\___|\__, |     )\n(                          |___/      )\n(    Tools for find credentials key   )\n(                  By ZeroByte.ID     )\n---------------------------------------''')
    args = argument()
    fakey = FAKey(args)
    try:
        fakey.scanning()
    except:
        print('[!] ERROR, Pleas try again!')
