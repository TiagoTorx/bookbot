def count_book_words(path):
    with open(path) as f:
        content = f.read()
        words = content.split()
    return len(words)

def get_num_characters(path):
    char_count = {}
    with open(path) as f:
        content = f.read()
        content = content.lower() 

        for char in content:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_list_of_char(char_count):
    filtered_items = [(char, count) for char, count in char_count.items() if char.isalpha()]
    sorted_items = sorted(filtered_items, key=lambda item: item[1], reverse=True)
    return [{'char': char, 'count': count} for char, count in sorted_items]