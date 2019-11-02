FROM ruby:2.6.5-alpine
WORKDIR /usr/src/app
COPY . .
RUN set -ex; apk add build-base sqlite-dev;
CMD ["/start.sh"]