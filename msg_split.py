from scripts.splitter import Splitter
from typing import Generator
import argparse


MAX_LEN = 4096


def split_message(source: str, max_len: int = MAX_LEN) -> Generator:
    """Splits the original message (`source`) into fragments of the specified length (`max_len`)."""
    html_splitter = Splitter(max_len)
    for fragment in html_splitter.split(source):
        yield from fragment


def main(args):
    file_path, max_len = args.file_path, args.max_len
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_source = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' nor found")
        return

    fragments = split_message(html_source, 4096)
    for fragment in fragments:
        print(f"fragment #: {len(fragment)} chars.")
        print(fragment)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Message split by length", argument_default="./examples/source.html")
    parser.add_argument(
        "--max-len",
        type=int,
        required=False,
        default=4096,
        help="The maxim length of fragments")
    parser.add_argument('file_path', type=str, help="The input Html file to split")
    args = parser.parse_args()
    main(args)
