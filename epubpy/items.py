from enum import Enum, auto
from functools import cached_property
from pathlib import Path
from typing import Any
from dataclasses import dataclass
from bs4 import BeautifulSoup


class ItemTypes(Enum):
    UNKNOWN = [auto()]
    IMAGE = ['.jpg', '.jpeg', '.gif', '.tiff', '.tif', '.png']
    STYLE = ['.css']
    JAVASCRIPT = ['.js']
    NAVIGATION = ['.ncx']
    VECTOR = ['.svg']
    FONT = ['.otf', '.woff', '.ttf']
    VIDEO = ['.mov', '.mp4', '.avi']
    AUDIO = ['.mp3', '.ogg']
    DOCUMENT = ['.htm', '.html', '.xhtml']
    SMIL = ['.smil']

    def __repr__(self):
        return self.__str__()   # Don't show the values as it is not needed


@dataclass
class Item:
    uid: str
    href: str | Path
    media_type: str
    base_path: str | Path
    media_overlay: str = None
    properties: str | Any = None
    fallback: Any = None

    @cached_property
    def type(self) -> ItemTypes:
        def guess():
            ext = Path(self.href).suffix
            for it in ItemTypes:
                if ext in it.value:
                    return it
            return ItemTypes.UNKNOWN

        match self.media_type:
            case "image/jpg" | "image/jpeg" | 'image/png' | 'image/svg+xml':
                return ItemTypes.IMAGE
            case 'application/x-dtbncx+xml':
                return ItemTypes.NAVIGATION
            case 'application/smil+xml':
                return ItemTypes.SMIL
            case 'application/xhtml+xml':
                return ItemTypes.DOCUMENT
            case _:
                return guess()

    @property
    def filepath(self) -> str | Path:
        """ This points to local file which the user can refer to read """
        return self.base_path.joinpath(self.href)

    def get_content(self, **kwargs) -> BeautifulSoup:
        """
        Here we parse the item content. Given kwargs are passed into underlying
        parser function
        """

        if self.type != ItemTypes.DOCUMENT:
            raise NotImplementedError(
                f"Reading support for {self.type} is not yet supported"
            )

        content = self.parse_html(**kwargs)
        return content

    def parse_html(self, features: str = 'lxml', **kwargs):

        # Read html from the file
        with open(self.filepath, "r") as f:
            bs = BeautifulSoup(f, features=features)

        return bs


@dataclass
class ItemRef:
    uid_ref: str
    uid: str = None
    linear: str = None
    properties: str | Any = None
