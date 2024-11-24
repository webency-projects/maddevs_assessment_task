from msg_split import split_message


def test_first():
    max_len = 4096
    file = "examples/source.html"
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    fragments = split_message(html, max_len)
    for fragment in fragments:
        assert len(fragment) <= max_len


def test_second():
    max_len = 4396
    answers = [4371, 1370]
    file = "examples/source.html"
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    fragments = split_message(html, max_len)
    for ans in answers:
        res = next(fragments)
        assert ans == len(res)


def test_third():
    max_len = 4296
    answers = [4249, 1492]
    file = "examples/source.html"
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    fragments = split_message(html, max_len)
    for ans in answers:
        res = next(fragments)
        assert ans == len(res)