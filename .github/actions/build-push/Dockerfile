FROM ruby:2.6.5-alpine
WORKDIR /github/workspace
COPY Gemfile ./
RUN set -ex; \
    apk add build-base sqlite-dev; \
    gem install bundler; \
    bundle install