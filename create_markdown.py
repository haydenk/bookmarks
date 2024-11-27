import duckdb
import json

# markdown: str = "# Bookmarks\n\n"

# categories = duckdb.sql("select distinct category from 'bookmarks.csv' order by category").fetchall()


# top: str = '|' * (len(categories) + 3)
# dividers: list = [':---:'] * (len(categories) + 2)
# links: list = [f" [{c[0].upper()}](#{c[0].replace('.', '')}) " for c in categories]

# markdown += f"{top}\n"
# markdown += f"|{'|'.join(dividers)}|\n"
# markdown += f"|{'|'.join(links)}|\n"

# for category in categories:
#     bookmarks = duckdb.sql(f"select title, url from 'bookmarks.csv' where category = '{category[0]}'")
#     markdown += f"\n\n\n### {category[0].upper()}\n\n"
#     for title, url in bookmarks.fetchall():
#         markdown += f"* [{title}]({url})\n"
#     markdown += "\n\n[Back to Top](#bookmarks)\n"

# with open('README.md', 'w+') as fp:
    # fp.write(markdown)

results = duckdb.sql("select * from 'new_bookmarks.csv';")

for id, title, domain, url in results.fetchall():
    print(id, title, domain, url)
    with open(f"tempData2/{id}.json", "w+") as fp:
        json.dump({'title': title, 'domain': domain, 'url': url}, fp)
