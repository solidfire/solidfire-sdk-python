#!/usr/bin/env bash
bumpversion --allow-dirty build
VERSION=$(grep "current_version" setup.cfg)
VERSION=${VERSION:18}
git submodule foreach 'git pull && git add . && git commit -m"Bump version to '$VERSION'" && git push || :'
git pull && git add . && git commit -m"Bump version to $VERSION" && git push
