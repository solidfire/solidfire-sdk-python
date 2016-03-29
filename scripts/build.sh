#!/bin/bash

# enable error reporting to the console
set -ev

echo $TOXENV

# only proceed script when started not by pull request (PR)
if [ "$TRAVIS_BRANCH" != release* ] || [ "$TOXENV" != "py35" ]; then
  echo "this is PR, exiting"
  exit 0
fi

#clone "master" branch of the repository using encrypted GH_TOKEN for authentification
git clone -b  gh-pages https://${GH_TOKEN}@github.com/solidfire/solidfire-sdk-python.git ../solidfire-sdk-python.gh-pages

# copy generated HTML site to "master" branch
cat ../solidfire-sdk-python.gh-pages/front.yml ./README.rst > ../solidfire-sdk-python.gh-pages/index.md

# commit and push generated content to `master' branch
# since repository was cloned in write mode with token auth - we can push there
cd ../solidfire-sdk-python.gh-pages
git config user.email "jason.womack@solidfire.com"
git config user.name "Jason Ryan Womack"
git add -A .
git commit -a -m "Travis #$TRAVIS_BUILD_NUMBER"
git push --quiet origin gh-pages > /dev/null 2>&1