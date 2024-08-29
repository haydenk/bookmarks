create table bookmarks
(
    title  VARCHAR(0),
    domain VARCHAR(0),
    url    VARCHAR(0),
    hash   CHAR(64) primary key
);

insert or replace into bookmarks (hash, title, domain, url)
select distinct sha256(url) as 'hash', title, domain, url
from read_csv('bookmarks.csv')
where regexp_matches(url, '^https?\:\/\/');

insert or replace into bookmarks (hash, title, domain, url)
select sha256(url) as 'hash'
     , title
     , regexp_replace(regexp_extract(url, '^https?\:\/\/([a-z0-9.-]+).*$', 1), '^www\.', '') as 'domain'
     , rtrim(regexp_replace(url, '(fbclid|pfb_.*|pd_.*|ref_|feature)=.*', ''), '?&') as 'url'
from read_json('data/*.json')
where regexp_matches(url, '^https?\:\/\/');

copy (select title, domain, url from bookmarks order by domain asc) to 'bookmarks.csv';

.mode markdown
select title, domain, url from bookmarks order by domain asc
