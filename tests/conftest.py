from pathlib import Path
from typing import Callable

from pytest import fixture


DATA_PATH = Path(__file__).parent.joinpath("data").resolve()


@fixture(scope="module")
def unzipped_path() -> Callable:
    def f(book: str | Path):
        return DATA_PATH.joinpath("unzipped", book)
    return f


@fixture(scope="module")
def datapath() -> Path:
    return DATA_PATH
