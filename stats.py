def get_num_words(text):
    number_of_words = 0
    list = text.split()
    for word in list:
        number_of_words += 1
    return number_of_words

def count_characters(text):
    char_count = {}
    text = text.lower()
    words = text.split()
    for word in words:
        for character in word:
            if str(character).isalpha():
                if character not in char_count:
                    char_count[character] = 1
                elif character in char_count:
                    char_count[character] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_dictionary(dictionary):
    list = []
    for x in dictionary:
        dict = { "char": x, "num": dictionary[x]}
        list.append(dict)

    list.sort(reverse=True, key=sort_on)
    return list
