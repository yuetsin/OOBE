#!/usr/bin/env python3

from os import path
from exec import popen
from printer import success, failure, information

def _update_brew():
    try:
        popen('brew update')
        success('updated homebrew')
    except:
        failure('failed to update homebrew')
        raise

def _update_pip():
    try:
        popen('pip3 install -U pip')
        success('updated pypi')
    except:
        failure('failed to update pip')
        raise

def _handle(dir: str):
    information('starting to handle module at `%s`' % dir)
    with open(path.join(dir, 'index.rb'), 'r') as f:
        lines = f.read().splitlines(keepends=False)

    head, lines = lines[0], [[w.strip() for w in v.split(':')] if ':' in v else (v.strip(), None) for v in lines[1:]]
    assert(head.startswith('$TYPE:'))

    category = head[6:].strip()
    if category == 'SUBFOLDERS':
        for name, _ in lines:
            try:
                _handle(path.join(dir, name))
            except:
                failure('error handling folder %s' % name)
                raise
    elif category == 'PYPI PACKAGES':
        _update_pip()
        for name, _ in lines:
            try:
                popen('pip3 install %s' % name)
                success('pypi package `%s` installed' % name)
            except:
                failure('error installing pypi package `%s`' % name)
                raise
    elif category == 'BREW RECIPES':
        _update_brew()
        for name, _ in lines:
            try:
                popen('brew install %s' % name)
                success('brew recipe `%s` installed' % name)
            except:
                failure('error installing brew recipe `%s`' % name)
                raise
    elif category == 'BREW CASK RECIPES':
        _update_brew()
        for name, _ in lines:
            try:
                popen('brew install --cask %s' % name)
                success('brew cask recipe `%s` installed' % name)
            except:
                failure('error installing brew cask recipe `%s`' % name)
                raise
    elif category == 'EXECUTABLES':
        for name, desc in lines:
            try:
                popen(path.join(dir, name))
                success('executable `%s`%s finished' % (name, ' (%s)' % desc if desc else ''))
            except:
                failure('error executing `%s`%s' % (name, ' (%s)' % desc if desc else ''))
                raise
    else:
        assert(not 'unknown category `%s`' % category)

if __name__ == '__main__':
    _handle('./')