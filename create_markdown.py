import duckdb

markdown: str = "# Bookmarks\n\n"

categories = duckdb.sql("select distinct left(domain, 1) as category from 'bookmarks.csv' order by domain").fetchall()

for category in categories:
    hash = category[0].replace('.', '')
    markdown += f"[{category[0].upper()}](#{hash})"
    if not category == categories[-1]:
        markdown += " | "

markdown += "\n\nHello World"
markdown = markdown.strip().rstrip('|').strip()

for category in categories:
    bookmarks = duckdb.sql(f"select title, url from 'bookmarks.csv' where domain like '{category[0]}%'")
    markdown += f"\n\n\n### {category[0].upper()}\n\n"
    for title, url in bookmarks.fetchall():
        markdown += f"* [{title}]({url})\n"
    markdown += "\n\n[Back to Top](#bookmarks)\n"

with open('README.md', 'w+') as fp:
    fp.write(markdown)