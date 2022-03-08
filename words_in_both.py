def words_in_both(string_1, string_2):
    """Takes two strings as parameters and returns a set of only those words that appear in both strings."""
    common_words = set()
    split_1 = string_1.lower().split()
    split_2 = string_2.lower().split()
    for words in split_1:
        if (words in split_2) and (words not in common_words):
            common_words.add(words)
    return common_words
