from stats import Number_of_words, number_of_each_letter, list_of_dictionaries
import sys 
def get_book_text(path_to_text):
    with open(path_to_text) as f:
        texti= f.read()
        return texti 
def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path=sys.argv[1]
    text=get_book_text(book_path)
    kirjainten_maara_sanakirja=number_of_each_letter(text)
    lista=list_of_dictionaries(kirjainten_maara_sanakirja)
    sanojen_maara=Number_of_words(text)
    print_book_report(book_path,sanojen_maara,lista)

def print_book_report(book_path,word_count,character_count):
    print("=====Bookbot======")
    print(f"Analyzing book found at {book_path}")
    print("----Word Count----")
    print(f"Found {word_count} total words")
    print("-----Character Count------")
    for i in character_count:
        if i["char"].isalpha()==False:
            continue
        print(f"{i["char"]}: {i["num"]}")
main()