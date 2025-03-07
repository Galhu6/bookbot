def word_count(book_text: str) -> int:
    count = len(book_text.split())
    return count

def sorted_char_count(book_text: str) -> dict[str, int]:
    char_count: dict[str, int] = {}

    for char in book_text:
        lower_char = char.lower() 
        char_count[lower_char] = char_count.get(lower_char, 0) + 1 

    return dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
                 
            
def to_sorted_list(char_dict: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)