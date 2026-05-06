from text_analyzer import average_word_length, count_words, top_words


def test_count_words_basic():
    assert count_words("a b c") == 3


def test_count_words_empty():
    assert count_words("") == 0


def test_average_word_length_empty():
    assert average_word_length("") == 0.0


def test_average_word_length_basic():
    assert average_word_length("ab cd ef") == 2.0


def test_top_words_basic():
    assert top_words("a a b", 1) == [("a", 2)]


def test_top_words_default_n():
    result = top_words("a a b b c d d d")
    assert len(result) == 3
    assert result[0] == ("d", 3)
