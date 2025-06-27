from stats import count_book_words, get_num_characters, sorted_list_of_char
import sys

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        pathfile = sys.argv[1]

    word_count = count_book_words(pathfile)
    characters_count = get_num_characters(pathfile)
    report = sorted_list_of_char(characters_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathfile}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in report:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()