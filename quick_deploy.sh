#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

jekyll build
git checkout _site/CNAME

mkdir -p git-rendered
rm -rf git-rendered/*
cp -r ./_site/* git-rendered/

cd git-rendered
git init
git add .
git commit -m "Updated"

git remote add origin "git@github.com:kuklinistvan/codekuklin.com.git"

echo Hit return to force push to GitHub
read

git push --force origin master

echo Hit return to remove git-rendered folder
read

cd ..
rm -rf git-rendered

echo Done
