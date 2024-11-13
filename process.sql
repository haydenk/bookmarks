copy (with recursive cte as (select distinct sha256(url) as 'hash'
     , title
     , regexp_replace(regexp_extract(url, '^https?\:\/\/([a-z0-9.-]+).*$', 1), '^www\.', '') as 'domain'
     , rtrim(regexp_replace(url, '(fbclid|pfb_.*|pd_.*|ref_|feature)=.*', ''), '?&') as 'url'
from read_json('bookmarks/*.json')
union all
select distinct sha256(url) as 'hash'
     , title
     , regexp_replace(regexp_extract(url, '^https?\:\/\/([a-z0-9.-]+).*$', 1), '^www\.', '') as 'domain'
     , rtrim(regexp_replace(url, '(fbclid|pfb_.*|pd_.*|ref_|feature)=.*', ''), '?&') as 'url'
from read_csv('bookmarks.csv')
where regexp_matches(url, '^https?\:\/\/'))
select cte.title, cte.domain, cte.url from cte) to 'new_bookmarks.csv';
