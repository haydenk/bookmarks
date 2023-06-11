import hashlib
import re
from abc import ABC
from urllib.parse import urlparse, ParseResult, parse_qsl


class Bookmark(object):
    url: str
    title: str
    domain: str
    url_checksum: str

    def __init__(self, url: str, title: str, domain: str = ""):
        self.url = url
        self.title = title
        self.domain = domain
        if not self.domain:
            self.domain = self.generate_domain()
        self.url = self.filter_trackers()
        self.url_checksum = hashlib.sha512(self.url.encode()).hexdigest()

    def __iter__(self):
        yield self.url
        yield self.title
        yield self.domain
        yield self.url_checksum

    def asdict(self) -> dict[str, str]:
        return {
            'title': self.title,
            'domain': self.domain,
            'url': self.url,
            'checksum': self.url_checksum,
        }

    def generate_domain(self) -> str:
        domain: str = urlparse(self.url).netloc
        domain = re.sub(r"^(www\.)", "", domain)
        return domain

    def filter_trackers(self) -> str:
        parsed_url: ParseResult = urlparse(self.url)
        new_qs: str = ""
        if "amazon.com" not in self.domain:
            for qs_key, qs_value in parse_qsl(parsed_url.query):
                if re.match(r"^utm", qs_key):
                    continue
                if re.match(r"^_yTrack", qs_key):
                    continue
                if re.match(r"^fbadid|fbclid|fbc_id|h_ad_id|rcstdid|li_fat_id|ad_id", qs_key):
                    continue
                new_qs += f"{qs_key}={qs_value}"
        new_url: str = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
        return f"{new_url}?{new_qs}" if new_qs else new_url


