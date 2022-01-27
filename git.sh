#!/bin/bash -x

date=$(date "+%Y%m%d")

git add -A
git commit -m "update: $date"
git push origin master
