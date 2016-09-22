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
git clone -b  gh-pages https://${GH_TOKEN}@github.com/solidfire/solidfire-sdk-java.git ../solidfire-sdk-java.gh-pages

cat ../solidfire-sdk-java.gh-pages/front.yml ./README.md > ../solidfire-sdk-java.gh-pages/index.md

# copy generated HTML site to `master' branch
for file in **/*.md; do
    cat ../solidfire-sdk-java.gh-pages/front.yml ${file} > ../solidfire-sdk-java.gh-pages/${file##*/}
done

sed -i -e 's/.md/.html/g' ../solidfire-sdk-java.gh-pages/*.md
sed -i -e 's/examples\///g' ../solidfire-sdk-java.gh-pages/*.md

rm -f ../solidfire-sdk-java.gh-pages/**/*.md-e

# commit and push generated content to `master' branch
# since repository was cloned in write mode with token auth - we can push there
cd ../solidfire-sdk-java.gh-pages
git config user.email "jason.womack@solidfire.com"
git config user.name "Jason Ryan Womack"
git add -A .
git commit --allow-empty -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --quiet origin gh-pages > /dev/null 2>&1
