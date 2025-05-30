def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_symbols(book_text):
    # get ful book, return dict with symbol and count
    symbols = {}
    words = book_text.split()
    for word in words:
        for symbol in word.lower():
            if symbol in symbols:
                symbols[symbol] += 1
            else:
                symbols[symbol] = 1
    return symbols

def sorted_symbols(symbols):
    formatted_list = []
    for char, count in symbols.items():
        formatted_list.append({"char": char, "num": count})
    formatted_list.sort(key=lambda x: x["num"], reverse=True)
    return formatted_list