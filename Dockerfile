FROM ruby:2.6.5-slim
WORKDIR /usr/src/app
COPY Gemfile ./
RUN set -ex; apt-get update; \
    apt-get install -y \
        build-essential \
        libsqlite3-dev; \
    bundle install