from scripts.tag import Tag


def test_name():
    tag = Tag("div", [])
    assert tag.name == "div"


def test_opening_tag_without_attributes():
    tag = Tag("div", [])
    assert tag.opening == "<div>"


def test_opening_tag_with_attributes():
    tag = Tag("input", [("type", "text"), ("value", "example")])
    assert tag.opening == '<input type="text" value="example">'


def test_closing_tag():
    tag = Tag("div", [])
    assert tag.closing == "</div>"


def test_repr():
    tag = Tag("span", [])
    assert repr(tag) == "span"
