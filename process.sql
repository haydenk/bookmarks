drop table bookmarks;
create table bookmarks
(
    title  VARCHAR(0),
    domain VARCHAR(0),
    url    VARCHAR(0),
    hash   CHAR(64) primary key
);

create table bookmarks as
select title
     , regexp_replace(regexp_extract(url, '^https?\:\/\/([a-z0-9.-]+).*$', 1), '^www\.', '') as 'domain'
     , rtrim(regexp_replace(url, '(fbclid|pfb_.*|pd_.*|ref_|feature)=.*', ''), '?&') as 'url'
     , sha256(url) as 'hash'
from read_csv('new.csv')
where regexp_matches(url, '^https?\:\/\/');

copy (select title, domain, url from bookmarks order by domain asc) to 'bookmarks.csv';
