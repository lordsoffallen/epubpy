from . import Books
from .data import TestData
from epubpy.content import get_opf_path, Metadata, Manifest, Spine
from epubpy.items import Item, ItemRef
from epubpy import Namespaces, check_type

from pathlib import Path
from pytest import mark, raises


def test_check_type():
    test_var = 1

    check_type("test_func", test_var, int, str)

    with raises(TypeError):
        check_type("test_func", test_var, str)


def test_get_opf_path():
    output = get_opf_path(TestData.META_INF_CONTAINER)

    assert output is not None  # Books have this path so it shouldn't be none
    assert output.split("/")[1].endswith(".opf")


@mark.parametrize("book", (Books.DRACULA, Books.LES_MISERABLES))
def test_get_opf_path_integration(unzipped_path, book):
    """ Test it with real book data """

    book_path = unzipped_path(book)
    opf_path = Path(book_path).joinpath("META-INF", "container.xml")

    with open(opf_path, "r") as f:
        meta_inf = f.read()

    output = get_opf_path(meta_inf)

    assert output is not None   # Books have this path so it shouldn't be none
    assert output.split("/")[1].endswith(".opf")


def test_metadata_parse():
    m = Metadata.from_content_opf(TestData.CONTENT_OPF)

    output = m.metadata

    namespaces = output.get_namespaces()
    assert len(namespaces) == 2
    assert all([ns for ns in namespaces if ns in [Namespaces.DC, Namespaces.OPF]])


def test_manifest_parse():
    m = Manifest.from_content_opf(TestData.CONTENT_OPF, opf_file_path="test")

    output = m.manifest

    assert output[0].type is not None       # run type property
    assert len(output) > 0
    assert all([isinstance(e, Item) for e in output])


def test_spine_parse():
    s = Spine.from_content_opf(TestData.CONTENT_OPF)

    output = s.spine

    assert len(output) > 0
    assert all([isinstance(e, ItemRef) for e in output])
