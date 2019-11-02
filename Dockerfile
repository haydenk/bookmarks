FROM ruby:2.6.5-alpine
WORKDIR /github/workspace
COPY Gemfile entrypoint.sh ./
RUN set -ex; \
    apk add build-base sqlite-dev; \
    gem install bundler; \
    chmod +x entrypoint.sh; \
    bundle install
ENTRYPOINT ["entrypoint.sh"]