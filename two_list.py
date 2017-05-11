
def count_words(test_file):

    data = open(test_file)

    word_list = []  # Create an empty list to store lists of [word, word count]
    word_content=[]
    word_count=[]# Create a dictionary to store word : word count pairs

    for line in data:
        line = line.rstrip()
        line = line.split(" ")
        word_list.extend(line)  # Extend list_of_words with all words from .txt

    print word_list

count_words("test.txt")
