def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words(text)} words found in the document")
    print("")
    #print(f" The Frankenstein book should contain {number_of_words(text)} words!")
    word_count = number_of_times_each_character(text)
    for word, count in sort_word_count(word_count):
        print(f"The word '{word}' appears {count} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    return len(text.split())
  
def number_of_times_each_character(text):
    word_count = {}
    for character in text:
        character = character.lower()
        if character in word_count:
            word_count[character] += 1
        else:
            word_count[character] = 1
    return word_count

def sort_word_count(word_count):
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)

main()
