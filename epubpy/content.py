from pathlib import Path
from io import BytesIO
from urllib.parse import unquote
from lxml import etree
from typing import Any
from collections import defaultdict

from . import Namespaces, check_type
from .items import Item, ItemRef


def parse_xml(s: str | bytes) -> etree.ElementTree:
    check_type(parse_xml.__name__, s, str, bytes)

    parser = etree.XMLParser(recover=True, resolve_entities=False)

    if isinstance(s, str):
        s = s.encode("utf-8")

    tree = etree.parse(BytesIO(s), parser=parser)

    return tree


def get_opf_path(meta_inf: str | bytes) -> str | None:
    """ Container file contains full path to OPF file """

    tree = parse_xml(meta_inf)
    container = tree.find(
        './/xmlns:rootfile[@media-type]',
        namespaces={'xmlns': Namespaces.CONTAINERS}
    )

    # Find the OPF file path
    if container.get('media-type') == 'application/oebps-package+xml':
        return container.get('full-path')


def parse_container(
    container: Any, field: str,
    return_uid: bool = False
) -> etree.Element:
    if isinstance(container, str) or isinstance(container, bytes):
        container = parse_xml(container)

    section = container.find('{%s}%s' % (Namespaces.OPF, field))

    if return_uid:
        uid = container.getroot().get('unique-identifier')
        return section, uid
    else:
        return section


class DefaultDict(defaultdict):
    def __repr__(self):
        return dict(self).__repr__()

    def __str__(self):
        return dict(self).__str__()


class NamespacedDict:
    def __init__(self):
        self.dict = DefaultDict(lambda: DefaultDict(list))

    def append(self, namespace: str, key: Any, value: Any, extras: Any):
        def f(d: Any) -> dict:
            return dict((k, v) for k, v in d.items())

        self.dict[namespace][key].append((value, f(extras)))

    def get_namespaces(self) -> list[str]:
        return list(self.dict.keys())

    def get(self, namespace: str, key: Any = None) -> Any:
        v = self.dict[namespace]
        if key is not None:
            v = v[key]
        return v

    def __repr__(self):
        return self.dict.__repr__()

    def __str__(self):
        return self.dict.__str__()


class Metadata:
    def __init__(self, metadata: etree.ElementTree, uid: str = None):
        self._metadata = metadata
        self.uid = uid

        self._nsdict = None

        # self.title = self.get(Namespaces.DC, 'title')[0][0]    # access the tuple
        # self.uid = self.get(Namespaces.DC, 'identifier')[0][0]

    @property
    def metadata(self):
        # here parse the content from self._metadata
        if self._nsdict is None:
            self._nsdict = self._parse()

        return self._nsdict

    @classmethod
    def from_content_opf(cls, container: Any) -> "Metadata":
        """ Read metadata section from content.opf file to create the class """

        metadata, uid = parse_container(container, field='metadata', return_uid=True)

        return cls(metadata, uid)

    def _parse(self) -> NamespacedDict:
        # lxml represents namespace with {namespace} so we apply the style here
        nsmap = {k: '{%s}' % v for k, v in self._metadata.nsmap.items()}
        default_ns = nsmap.get(None, "")
        nsdict = NamespacedDict()

        for e in self._metadata:
            if not etree.iselement(e) or e.tag is etree.Comment:
                continue

            if e.tag == default_ns + 'meta':
                prefix, name = None, e.get('name')

                if name is not None and ':' in name:
                    prefix, name = name.split(':', 1)

                nsdict.append(
                    namespace=e.nsmap.get(prefix, prefix),
                    key=name,
                    value=e.text,
                    extras=e
                )
            else:
                # Didn't match meta value
                tag = e.tag[e.tag.rfind('}') + 1:]      # remove namespace from the str

                # <dc:identifier id="uid">     # checks for this field
                if (e.prefix and e.prefix.lower() == 'dc') and tag == 'identifier':
                    self.uid = e.get('id', self.uid)      # update uid if founded, else same

                nsdict.append(
                    namespace=e.nsmap[e.prefix], key=tag, value=e.text, extras=e
                )

        return nsdict


class Manifest:
    def __init__(self, manifest: etree.ElementTree, base_path: str | Path):
        self._manifest = manifest
        self.base_path = Path(base_path)

        self._items = None

    @property
    def manifest(self):
        # here parse the content from self._manifest
        if self._items is None:
            self._items = self._parse()

        return self._items

    @classmethod
    def from_content_opf(cls, container: Any, base_path: str | Path) -> "Manifest":
        manifest = parse_container(container, 'manifest')

        return cls(manifest, base_path)

    def _parse(self) -> list[Item]:

        items = []

        for e in self._manifest:
            if e is not None and e.tag != '{%s}item' % Namespaces.OPF:
                continue

            items.append(
                Item(
                    uid=e.get('id'),
                    href=unquote(e.get('href')),
                    media_type=e.get('media-type'),
                    base_path=self.base_path,
                    properties=e.get('properties'),
                    fallback=e.get('fallback'),
                )
            )

        return items


class Spine:
    def __init__(self, spine: etree.ElementTree):
        self._spine = spine
        self.toc = spine.get('toc')
        self.direction = spine.get('page-progression-direction')

        self._page_orders = None

    @property
    def spine(self):
        if self._page_orders is None:
            self._page_orders = self._parse()

        return self._page_orders

    @classmethod
    def from_content_opf(cls, container: Any) -> "Spine":
        spine = parse_container(container, field='spine')
        return cls(spine)

    def _parse(self) -> list[ItemRef]:
        return [
            ItemRef(
                uid_ref=t.get('idref'),
                uid=t.get('id'),
                linear=t.get('linear', 'yes'),
                properties=t.get('properties'),
            )
            for t in self._spine
        ]
