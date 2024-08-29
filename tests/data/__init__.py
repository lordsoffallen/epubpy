class TestData:
    META_INF_CONTAINER = """
    <?xml version='1.0' encoding='utf-8'?>
        <container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0">
          <rootfiles>
            <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
          </rootfiles>
        </container>
    """

    CONTENT_OPF = """
    <?xml version="1.0" encoding="utf-8"?>
        <package xmlns="http://www.idpf.org/2007/opf" dir="ltr" prefix="se: https://standardebooks.org/vocab/1.0" unique-identifier="uid" version="3.0" xml:lang="en-US">
            <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
                <dc:identifier id="uid">url:https://standardebooks.org/ebooks/victor-hugo/les-miserables/isabel-f-hapgood</dc:identifier>
                <dc:date>2019-08-15T21:23:54Z</dc:date>
                <meta property="dcterms:modified">2024-08-22T05:53:22Z</meta>
                <meta property="se:revision-number">0</meta>
                <dc:publisher id="publisher">Standard Ebooks</dc:publisher>
                <meta property="file-as" refines="#publisher">Standard Ebooks</meta>
                <meta property="se:url.homepage" refines="#publisher">https://standardebooks.org</meta>
                <dc:contributor id="type-designer">The League of Moveable Type</dc:contributor>
                <dc:title id="title">Les Misérables</dc:title>
                <meta property="file-as" refines="#title">Les Misérables</meta>
                <link href="onix.xml" media-type="application/xml" properties="onix" rel="record"/>
                <meta id="collection-1" property="belongs-to-collection">Haycraft-Queen Cornerstones</meta>
                <meta property="collection-type" refines="#collection-1">set</meta>
                <dc:description id="description">An escaped convict steals two candlesticks and uses the proceeds to redeem himself and become an honest man.</dc:description>
                <dc:language>en-US</dc:language>
                <dc:source>https://www.gutenberg.org/ebooks/135</dc:source>
                <dc:source>https://archive.org/details/in.ernet.dli.2015.149684</dc:source>
                <meta property="se:url.encyclopedia.wikipedia">https://en.wikipedia.org/wiki/Les_Mis%C3%A9rables</meta>
                <meta property="se:url.vcs.github">https://github.com/standardebooks/victor-hugo_les-miserables_isabel-f-hapgood</meta>
                <meta property="se:word-count">562297</meta>
                <meta property="se:reading-ease.flesch">71.44</meta>
                <dc:creator id="author">Victor Hugo</dc:creator>
                <dc:contributor id="translator">Isabel F. Hapgood</dc:contributor>
                <meta property="file-as" refines="#translator">Hapgood, Isabel F.</meta>
                <dc:contributor id="transcriber-1">Judith Boss</dc:contributor>
                <meta property="file-as" refines="#transcriber-1">Boss, Judith</meta>
                <meta property="role" refines="#transcriber-1" scheme="marc:relators">trc</meta>
                <dc:contributor id="transcriber-2">David Widger</dc:contributor>
                <meta property="file-as" refines="#transcriber-2">Widger, David</meta>
                <meta property="se:url.authority.nacoaf" refines="#transcriber-2">http://id.loc.gov/authorities/names/no2011017869</meta>
                <meta property="role" refines="#transcriber-2" scheme="marc:relators">trc</meta>
                <dc:contributor id="producer-1">Michael Atkinson</dc:contributor>
                <meta property="file-as" refines="#producer-1">Atkinson, Michael</meta>
                <meta property="se:url.homepage" refines="#producer-1">https://github.org/michael-77</meta>
                <dc:contributor id="producer-2">Robin Whittleton</dc:contributor>
                <meta property="file-as" refines="#producer-2">Whittleton, Robin</meta>
                <meta property="se:url.homepage" refines="#producer-2">http://www.robinwhittleton.com</meta>
                <meta property="role" refines="#producer-2" scheme="marc:relators">pfr</meta>
                <meta property="se:built-with">2.7.1</meta>
                <meta name="cover" content="cover.jpg"/>
            </metadata>
            <manifest>
                <item href="css/core.css" id="core.css" media-type="text/css"/>
                <item href="css/local.css" id="local.css" media-type="text/css"/>
                <item href="css/se.css" id="se.css" media-type="text/css"/>
                <item href="images/banknote.png" id="banknote.png" media-type="image/png"/>
                <item href="images/cover.jpg" id="cover.jpg" media-type="image/jpeg" properties="cover-image"/>
                <item href="images/logo.png" id="logo.png" media-type="image/png"/>
                <item href="images/titlepage.png" id="titlepage.png" media-type="image/png"/>
                <item href="text/book-1-1.xhtml" id="book-1-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/book-1-2.xhtml" id="book-1-2.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/book-1-3.xhtml" id="book-1-3.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/book-2-1.xhtml" id="book-2-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/book-2-2.xhtml" id="book-2-2.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/chapter-1-1-1.xhtml" id="chapter-1-1-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/chapter-1-2-1.xhtml" id="chapter-1-2-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/chapter-1-3-1.xhtml" id="chapter-1-3-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/chapter-2-1-1.xhtml" id="chapter-2-1-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/chapter-2-2-1.xhtml" id="chapter-2-2-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/colophon.xhtml" id="colophon.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/endnotes.xhtml" id="endnotes.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/halftitlepage.xhtml" id="halftitlepage.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/imprint.xhtml" id="imprint.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/loi.xhtml" id="loi.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/preface.xhtml" id="preface.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/titlepage.xhtml" id="titlepage.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/uncopyright.xhtml" id="uncopyright.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/volume-1.xhtml" id="volume-1.xhtml" media-type="application/xhtml+xml"/>
                <item href="text/volume-2.xhtml" id="volume-2.xhtml" media-type="application/xhtml+xml"/>
                <item href="toc.xhtml" id="toc.xhtml" media-type="application/xhtml+xml" properties="nav"/>
                <item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml"/>
            </manifest>
            <spine toc="ncx">
                <itemref idref="titlepage.xhtml"/>
                <itemref idref="imprint.xhtml"/>
                <itemref idref="preface.xhtml"/>
                <itemref idref="halftitlepage.xhtml"/>
                <itemref idref="volume-1.xhtml"/>
                <itemref idref="book-1-1.xhtml"/>
                <itemref idref="chapter-1-1-1.xhtml"/>
                <itemref idref="book-1-2.xhtml"/>
                <itemref idref="chapter-1-2-1.xhtml"/>
                <itemref idref="book-1-3.xhtml"/>
                <itemref idref="chapter-1-3-1.xhtml"/>
                <itemref idref="volume-2.xhtml"/>
                <itemref idref="book-2-1.xhtml"/>
                <itemref idref="chapter-2-1-1.xhtml"/>
                <itemref idref="book-2-2.xhtml"/>
                <itemref idref="chapter-2-2-1.xhtml"/>
                <itemref idref="endnotes.xhtml"/>
                <itemref idref="loi.xhtml"/>
                <itemref idref="colophon.xhtml"/>
                <itemref idref="uncopyright.xhtml"/>
            </spine>
            <guide>
                <reference href="text/titlepage.xhtml" title="Titlepage" type="title-page"/>
                <reference href="text/endnotes.xhtml" title="Endnotes" type="notes"/>
                <reference href="text/loi.xhtml" title="List of Illustrations" type="loi"/>
            </guide>
        </package>

    
    """
