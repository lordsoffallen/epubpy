from pathlib import Path
from logging import getLogger
from bs4 import BeautifulSoup

from .content import Manifest, Metadata, Spine, get_opf_path, NamespacedDict
from .items import Item, ItemRef, ItemTypes

import zipfile as zf


__all__ = [
    "EpubBook",
    "read_epub"
]

logger = getLogger(__file__)


class EpubBook:
    def __init__(self, metadata: Metadata, manifest: Manifest, spine: Spine):
        self._metadata = metadata
        self._manifest = manifest
        self._spine = spine

    @property
    def metadata(self) -> NamespacedDict:
        return self._metadata.metadata

    @property
    def manifest(self) -> list[Item]:
        return self._manifest.manifest

    @property
    def spine(self) -> list[ItemRef]:
        return self._spine.spine

    def get_spine_items(self) -> list[Item]:
        """ Map item refs to items here and return them """
        items = []

        for ref in self.spine:
            for it in self.manifest:
                if ref.uid_ref == it.uid:
                    items.append(it)
                    break   # There is a single match so break out of the first loop
        return items

    def to_bs4(self) -> list[BeautifulSoup]:
        """ Convert list of Item to bs4 representations. Filters only Document items """

        items = self.get_spine_items()

        contents = []

        for it in items:
            if it.type == ItemTypes.DOCUMENT:
                contents.append(it.get_content())  # returns bs4 content

        return contents


def read_epub(file_path: str | Path, extract_to: str = "unzipped") -> EpubBook:
    """
    Read an epub file from a given path.

    Parameters
    ----------
    file_path: str | Path
        File path to the epub file
    extract_to: str
        String that defines the name of the directory files will be extract to

    Returns
    -------
    EpubBook
        Returns a created EpubBook class instance
    """

    if isinstance(file_path, str):
        file_path = Path(file_path)

    file_name = file_path.stem
    extraction_dir = file_path.parent.joinpath(extract_to, file_name)

    # Check if the extraction directory already exists
    if not extraction_dir.exists():
        with zf.ZipFile(
            file_path,
            "r",
            compression=zf.ZIP_DEFLATED,
            allowZip64=True
        ) as zipped:
            zipped.extractall(extraction_dir)
    else:
        logger.info(f"Skipping extraction, '{extraction_dir}' already exists.")

    def read(path: Path | str):
        with open(extraction_dir.joinpath(path), "r") as f:
            return f.read()

    meta_inf = read(Path("META-INF", "container.xml"))
    opf_path = get_opf_path(meta_inf)
    opf = read(opf_path)

    # Parse content.opf file
    metadata = Metadata.from_content_opf(opf)


    manifest = Manifest.from_content_opf(
        opf,
        # Here find the base path that href refers to
        base_path=extraction_dir.joinpath(Path(opf_path).parent)
    )
    spine = Spine.from_content_opf(opf)

    return EpubBook(
        metadata=metadata, manifest=manifest, spine=spine
    )
