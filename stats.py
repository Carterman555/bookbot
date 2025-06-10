

def get_word_count(text):
    word_count = len(text.split())
    return word_count


def get_char_counts(text):

    char_dict = {}
    for char in text:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1


    return char_dict

def get_sorted_char_counts(char_counts):

    sorted_char_counts = []

    for char, count in char_counts.items():

        if not char.isalpha():
            continue

        current_char_dict = {"char": char, "num": count}
        sorted_char_counts.append(current_char_dict)

    sorted_char_counts.sort(reverse=True, key=lambda dict: dict["num"])

    return sorted_char_counts
