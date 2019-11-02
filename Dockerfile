FROM ruby:2.6.5-alpine
WORKDIR /github/workspace
COPY Gemfile ./
COPY entrypoint.sh ./
RUN set -ex; \
    apk add build-base sqlite-dev; \
    gem install bundler; \
    bundle install
CMD ["bundle", "exec", "ruby", "get_bookmarks.rb"]