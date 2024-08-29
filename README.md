# epubpy

A lightweight epub reader library in python. It converts epub html/xhtml files to
bs4 and from there further processing can be done. 

```python

from epubpy.epub import read_epub

book = read_epub("path/to/book.epub")   # is instance of EpubBook

# Access the epub metadata
book.metadata

# Access the manifest file which contains the list of all files
book.manifest

# Access the spine which is indicating the book read order
book.spine

# Get a list of items based on read order
items = book.get_spine_items()      # list of Item

items[0].get_content()  # returns a BeautifulSoup obj from the file
```

# Requirements

Project uses `beautifulsoup4, lxml` packages. 

# Installation ## TODO

```shell
conda install -c conda-forge epubpy
```