def count_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    statistics = dict()
    for char in text:
        count = statistics.get(char.lower(), 0)
        statistics[char.lower()] = count + 1
    return statistics


def sort_on(dictionary):
    return dictionary["num"]


def generate_sorted_list(stats):
    result = []
    for key, value in stats.items():
        result.append({"char": key, "num": value})
    result.sort(reverse=True, key=sort_on)
    return result