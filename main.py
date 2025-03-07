import sys
from stats import sorted_char_count, word_count, to_sorted_list

def get_book_text(filepath: str) -> str:
    try:
        with open(filepath, encoding="utf-8") as f:
            file_contents = f.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)



def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    book_text = get_book_text(file_path)
    
    total_words = word_count(book_text) 
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    
    char_freq = sorted_char_count(book_text) 
     
    print("--------- Character Count -------")
    sorted_list = to_sorted_list(char_freq)

    for char, count in sorted_list:
        if char.strip().isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
