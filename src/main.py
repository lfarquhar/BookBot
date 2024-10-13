def count_words(file_path):
    number_of_words = 0

    with open(file_path) as f:
        file_contents = f.read()
        number_of_words = len(file_contents.split())
    
    return number_of_words


def count_characters(txt):
    char_counts = {}

    lowercase_txt = txt.lower()

    for char in lowercase_txt:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def get_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():

    txt = get_text("books/frankenstein.txt")
    cnt_dictionary = count_characters(txt)

    for entry, value in cnt_dictionary.items():
        print(f"The '{entry}' character was found {value} times.")

main()