#!/usr/bin/env python3

from colorama import Fore, Style

def information(info: str):
    print(Fore.YELLOW, Style.BRIGHT, '::::: ', Style.RESET_ALL, info, sep='')

def success(info: str):
    print(Fore.GREEN, Style.BRIGHT, '[^_^] ', Style.RESET_ALL, info, sep='')

def failure(info: str):
    print(Fore.RED, Style.BRIGHT, '[*_*] ', Style.RESET_ALL, info, sep='')
