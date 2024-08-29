from epubpy.epub import read_epub, EpubBook
from pytest import mark

from . import Books


@mark.parametrize("book", (Books.DRACULA, Books.LES_MISERABLES))
def test_read_epub(datapath, book):
    epub_path = datapath.joinpath(f"{book}.epub")

    book = read_epub(epub_path)

    it = book.get_spine_items()

    for i in it:
        c = i.get_content()

    assert book.metadata is not None
    assert book.manifest is not None
    assert book.spine is not None
