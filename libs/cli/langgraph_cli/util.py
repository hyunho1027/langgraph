import os
from typing import Optional


def clean_empty_lines(input_str: str):
    return "\n".join(filter(None, input_str.splitlines()))


def urljoin(base: Optional[str], url: str) -> str:
    if base is None:
        return url

    return os.path.join(base, url)
