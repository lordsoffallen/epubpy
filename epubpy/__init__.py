from typing import Any


def check_type(fname: str, var: Any, *types):
    """
    Given a function name, variable and types, raise value error in case of type mismatch

    Parameters
    ----------
    fname: str
        Name of the function
    var: Any
        Variable itself
    types: Any
        Types to check variable on

    Raises
    -------
    TypeError
        If var and types mismatch
    """

    if not any([isinstance(var, t) for t in types]):
        raise TypeError(f"Function {fname} expected {types} but got {type(var)}")


class EpubException(Exception):

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class Namespaces:
    XML: str = 'http://www.w3.org/XML/1998/namespace'
    EPUB: str = 'http://www.idpf.org/2007/ops'
    DAISY: str = 'http://www.daisy.org/z3986/2005/ncx/'
    OPF: str = 'http://www.idpf.org/2007/opf'
    CONTAINERS: str = 'urn:oasis:names:tc:opendocument:xmlns:container'
    DC: str = 'http://purl.org/dc/elements/1.1/'
    XHTML: str = 'http://www.w3.org/1999/xhtml'
