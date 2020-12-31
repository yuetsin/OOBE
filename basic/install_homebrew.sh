#!/usr/bin/env bash 

git clone --depth=1 https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/install.git brew-install
/bin/bash -c "$(sed 's|^BREW_REPO=.*$|BREW_REPO="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"|g' brew-install/install.sh)"
rm -rf brew-install
