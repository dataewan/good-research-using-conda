from zipfs_law import parse_text


def test_sample_data():
    with open("tests/sample_data.txt", "r") as f:
        assert parse_text.count_words(f, True) == {
            'the': 5, 'and': 4, 'i': 3, 'to': 2, 'of': 1}
