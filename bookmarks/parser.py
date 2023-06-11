import configparser
import plistlib
from abc import abstractmethod
from dataclasses import dataclass
from hashlib import sha256
from os.path import splitext, basename
from urllib.parse import urlparse

import magic


@dataclass
class Parser(object):
    url: str
    title: str
    domain: str
    bookmark_source: str

    def __init__(self, source_filename: str):
        self.bookmark_source = source_filename
        self.title, self.domain, self.url = self.parse()

    def asdict(self) -> dict[str, str]:
        return {
            'title': self.title,
            'domain': self.domain,
            'url': self.url,
        }

    @abstractmethod
    def parse(self):
        pass

    @staticmethod
    def create(source_filename: str):
        file_type: str = magic.from_file(source_filename)
        if "MS Windows 95 Internet shortcut text" in file_type:
            return InternetShortcut(source_filename)
        elif "Apple binary property list" in file_type:
            return Webloc(source_filename)
        raise Exception("Unable to determine bookmark type")


class Webloc(Parser, object):
    def __init__(self, source_filename: str):
        super().__init__(source_filename)

    def parse(self):
        filename, file_ext = splitext(self.bookmark_source)
        title: str = basename(filename.strip('.')).strip()
        with open(self.bookmark_source, "rb") as fp:
            bookmark_data: dict = plistlib.load(fp)
        domain: str = urlparse(bookmark_data.get('URL').strip()).netloc
        return title, domain, bookmark_data.get('URL')


class InternetShortcut(Parser, object):
    def __init__(self, source_filename: str):
        super().__init__(source_filename)

    def parse(self):
        filename, file_ext = splitext(self.bookmark_source)
        title: str = basename(filename.strip('.')).strip()
        config = configparser.ConfigParser()
        config.read(self.bookmark_source)
        url: str = config.get('InternetShortcut', 'url').strip()
        domain: str = urlparse(url).netloc.strip()
        return title, domain, url
