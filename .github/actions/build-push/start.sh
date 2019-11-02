set -ex

gem install bundler
bundle install

git config --local user.email "action@github.com"
git config --local user.name "GitHub Action"
git add -f README.md bookmarks.csv
git commit -m "Add changes" -a

remote_repo="https://${GITHUB_ACTOR}:${INPUT_GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
git push "${remote_repo}" HEAD:master --follow-tags $_FORCE_OPTION
