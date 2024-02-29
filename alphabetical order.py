def sort_words(sentence):
    words = sentence.split()
    sorted_words = sorted(words)
    return sorted_words
if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    sorted_words = sort_words(sentence)
    print("Sorted words:", sorted_words)
