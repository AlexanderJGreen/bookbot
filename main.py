from stats import word_count, count_characters, sorted_character_counts
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else: 
    file_path = sys.argv[1] 


def get_book_text(file_path):
    with open(file_path) as f:
        contents = f.read()
        return contents
    
def main():
    # file_path = "books/frankenstein.txt"
    book_contents = get_book_text(file_path)


    word_amounts = word_count(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_amounts} total words")
    
    char_counts = count_characters(book_contents)

    sorted_counts = sorted_character_counts(char_counts)
    print("--------- Character Count -------")
    for entry in sorted_counts:
        char = entry["character"]
        count = entry["count"]
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    
    print("============= END ===============")

main()

