
def count_word_occurrences(sentence: str) -> tuple[dict[str, int], str | None, int]:
    word_count = {}
    words = sentence.split()
    length = 0
    long_word = None
    for word in words:
        word = word.lower()
        if len(word) > length:
            length = len(word)
            long_word = word
        word = ''.join(char for char in word if char.isalnum())
        if word in word_count:
            word_count[word.capitalize()] += 1
        else:
            word_count[word.capitalize()] = 1

    return word_count, long_word, length


def st_reverse(st: str) -> list[str]:
    return st.split(" ")[::-1]


# Example usage
sentence = "Hello world! Hello everyone. Welcome to the world of Python."
print(count_word_occurrences(sentence))
print(st_reverse(sentence))
