def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    statistics = dict()
    for char in text:
        count = statistics.get(char.lower(), 0)
        statistics[char.lower()] = count + 1
    return statistics