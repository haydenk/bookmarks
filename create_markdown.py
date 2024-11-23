import duckdb

markdown: str = ""

categories = duckdb.sql("select distinct domain from 'bookmarks.csv' order by domain").fetchall()

for category in categories:
    hash = category[0].replace('.', '')
    markdown += f"* [{category[0]}](#{hash})\n"

markdown += "\n\n"

for category in categories:
    bookmarks = duckdb.sql(f"select title, url from 'bookmarks.csv' where domain = '{category[0]}'")
    markdown += f"### {category[0]}\n\n"
    for title, url in bookmarks.fetchall():
        markdown += f"* [{title}]({url})\n"
    markdown += "\n\n[Back to Top]()\n"

with open('README.md', 'w+') as fp:
    fp.write(markdown)