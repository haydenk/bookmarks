import duckdb
import json

results = duckdb.sql("select cast(uuid() as string) as id, title, domain, url from read_csv('bookmarks.csv')")

for id, title, domain, url in results.fetchall():
    data: dict = {
        'id': id,
        'title': title,
        'domain': domain,
        'url': url
    }
    filename: str = f"bookmarks/{id}.json"
    print(f"Saving to {filename}")
    print(data)
    with open(filename, "w+") as fp:
        json.dump(data, fp)
