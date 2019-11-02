FROM ruby:2.6.5-alpine
WORKDIR /usr/src/app
COPY Gemfile entrypoint.sh ./
RUN set -ex; \
    apk add build-base sqlite-dev; \
    gem install bundler; \
    bundle install
ENTRYPOINT ["entrypoint.sh"]