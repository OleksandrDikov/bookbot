from stats import get_num_words, get_num_symbols, sorted_symbols
import sys

def get_book_text(book_id):
    with open(book_id, "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_id = sys.argv[1]

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {book_id}...")
    book_text = get_book_text(book_id)

    print("----------- Word Count ----------")
    words = get_num_words(book_text)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    symbols = get_num_symbols(book_text)
    sorted_symbols_list = sorted_symbols(symbols)
    for sym in sorted_symbols_list:
        if sym['char'].isalpha():
            print(f"{sym['char']}: {sym['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
