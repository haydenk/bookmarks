import duckdb

markdown: str = "# Bookmarks\n\n"

categories = duckdb.sql("select distinct left(domain, 1) as category from 'bookmarks.csv' order by domain").fetchall()


top: str = '|' * (len(categories) + 2)
dividers: list = [':---:'] * (len(categories) + 2)
links: list = [f"[{c[0].upper()}](#{c[0].upper().replace('.', '')})" for c in categories]

markdown += f"{top}\n"
markdown += f"|{'|'.join(dividers)}|\n"
markdown += f"|{'|'.join(links)}|\n"

for category in categories:
    bookmarks = duckdb.sql(f"select title, url from 'bookmarks.csv' where domain like '{category[0]}%'")
    markdown += f"\n\n\n### {category[0].upper()}\n\n"
    for title, url in bookmarks.fetchall():
        markdown += f"* [{title}]({url})\n"
    markdown += "\n\n[Back to Top](#bookmarks)\n"

with open('README.md', 'w+') as fp:
    fp.write(markdown)