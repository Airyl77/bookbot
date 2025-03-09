def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def count_characters(file_contents):
    num_char = dict()
    for char in file_contents:
        char_lower = char.lower()
        if char_lower in num_char:
            num_char[char.lower()] += 1
        else:
            num_char[char.lower()] = 1
    return num_char

def sort_on(dict):
    return dict["num"]

def sort_dict(dict_var):
    list = []
    for char, num in dict_var.items():
        dict_item = dict()
        dict_item["char"]=char
        dict_item["num"]=num
        list.append(dict_item)
    list.sort(reverse=True, key=sort_on)
    return list
