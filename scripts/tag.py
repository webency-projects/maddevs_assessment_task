from typing import List, Tuple


class Tag:
    def __init__(self, tag: str, attrs: List[Tuple[str, str | None]]):
        self._tag = tag
        self._attrs = attrs

    @property
    def name(self) -> str:
        return self._tag

    @property
    def opening(self) -> str:
        attributes = ' '.join(f'{a[0]}="{a[1]}"' for a in self._attrs)
        return f'<{self._tag}>' if not attributes else f'<{self._tag} {attributes}>'

    @property
    def closing(self) -> str:
        return f'</{self._tag}>'

    def __repr__(self):
        return self._tag

