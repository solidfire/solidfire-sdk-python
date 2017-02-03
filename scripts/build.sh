#!/bin/bash

# only proceed script when started on master
if [ $TRAVIS_BRANCH != "master" ]; then
  echo "this is not on master, exiting"
  exit 0
fi

# only proceed script when started not by pull request (PR)
if [ $TRAVIS_PULL_REQUEST == "true" ]; then
  echo "this is PR, exiting"
  exit 0
fi

# enable error reporting to the console
set -e

#clone `master' branch of the repository using encrypted GH_TOKEN for authentification
git clone -b  gh-pages https://${GH_TOKEN}@github.com/solidfire/solidfire-sdk-python.git ../solidfire-sdk-python.gh-pages

{ cat ../solidfire-sdk-python.gh-pages/front.yml ; pandoc -s -f rst --to=markdown_github ./README.rst ; } > ../solidfire-sdk-python.gh-pages/index.md

# copy generated HTML site to `master' branch
for file in examples/*.rst; do
    filename="${file##*/}"
    filenameWithoutExtension="${filename%.*}"
    { cat ../solidfire-sdk-python.gh-pages/front.yml ; pandoc -s -f rst --to=markdown_github ${file} ; } > ../solidfire-sdk-python.gh-pages/${filenameWithoutExtension}.md
done

sed -i -e 's/.rst/.html/g' ../solidfire-sdk-python.gh-pages/*.md
sed -i -e 's/examples\///g' ../solidfire-sdk-python.gh-pages/*.md

rm -f ../solidfire-sdk-python.gh-pages/**/*.md-e

# commit and push generated content to `master' branch
# since repository was cloned in write mode with token auth - we can push there
cd ../solidfire-sdk-python.gh-pages
git config user.email "adam.haid@solidfire.com"
git config user.name "Adam Haid"
git add -A .
git commit --allow-empty -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --quiet origin gh-pages > /dev/null 2>&1
