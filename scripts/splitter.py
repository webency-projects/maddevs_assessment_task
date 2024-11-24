from typing import List, Tuple
from scripts.tag import Tag
from scripts.exceptions import SplitException


class Splitter:
    def __init__(self, max_len: int):
        self.__max_len: int = max_len
        self.__fragments: List[str] = []
        self.__current: List[str] = []
        self.__stack: List[Tag] = []

    def split(self, text: str):
        self._parsing(text)
        yield self.__fragments
        self._reset()

    def _parsing(self, data):
        while '>' in data:
            idx = data.index('<')
            tag_data, data = data[:idx], data[idx + 1:]
            if tag_data:
                self._handle_data(tag_data)

            idx = data.index('>')
            tag_data, data = data[:idx], data[idx + 1:]
            if tag_data.startswith('/'):
                if not self.__stack or self.__stack[-1].name != tag_data[1:]:
                    raise ValueError('Invalid Html tag')
                self.__current.append(self.__stack.pop().closing)
            else:
                elements = tag_data.split()
                attrs = []
                tag = elements[0]
                if len(elements) > 1:
                    for element in elements[1:]:
                        attr_0, *attr_1 = element.split('=')
                        attr_1 = "=".join(attr_1) if len(attr_1) > 1 else attr_1[0]
                        attrs.append((attr_0, attr_1[1:-1]))

                self._hande_starttag(tag, attrs)
        if data:
            self._handle_data(data)
        self._split()

    def _hande_starttag(self, tag: str, attrs: List[Tuple[str, str]]):
        html_tag = Tag(tag, attrs)
        self.__stack.append(html_tag)
        self.__current.append(html_tag.opening)
        if self._delta >= 0:
            top_tag = self.__stack.pop()
            top = self.__current.pop()
            self._split()
            self.__stack.append(top_tag)
            self.__current.append(top)
            if self._delta >= 0:
                raise SplitException

    def _handle_data(self, data):
        self.__current.append(data)
        delta = self._delta
        while delta > 0:
            data = self.__current.pop()
            self.__current.append(data[:-delta])
            self._split()
            self.__current.append(data[-delta:])
            delta = self._delta

    def _split(self):
        closed_part = self._tags_to_string(self._to_close_current)
        if not closed_part:
            raise SplitException
        self.__fragments.append(closed_part)
        self.__current = []
        self.__current.extend(self._opening_tags)

    def _reset(self):
        self.__fragments = []
        self.__current = []
        self.__stack = []

    @property
    def _opening_tags(self) -> List[str]:
        return [t.opening for t in self.__stack]

    @property
    def _closing_tags(self) -> List[str]:
        return [t.closing for t in reversed(self.__stack)]

    @property
    def _to_close_current(self) -> List[str]:
        return self.__current + self._closing_tags

    @staticmethod
    def _tags_to_string(tags: List[str]) -> str:
        return ''.join(tags)

    @property
    def _delta(self) -> int:
        closed = self._to_close_current
        return len(self._tags_to_string(closed)) - self.__max_len




