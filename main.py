import sys
from stats import GetWordCount
from stats import CountCharacters
from stats import SortedReport


book = "books/frankenstein.txt"

def GetBookText(filepath):
    with open(filepath) as f:       
        s = f.read()
        return s






def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book = sys.argv[1]

    _count = GetWordCount(GetBookText(book))
    #print(f"{_count} words found in the document")
    _characters = CountCharacters(GetBookText(book))
    #print(_characters)
    sorted_list = SortedReport(_characters)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {_count} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        if entry[0].isalpha():
            print(f"{entry[0]}: {entry[1]}")
    print("============= END ===============")





main()
