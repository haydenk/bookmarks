FROM ruby:2.6.5-alpine
COPY . /
RUN set -ex; apk add --no-cache build-base sqlite-dev;
CMD ["/start.sh"]