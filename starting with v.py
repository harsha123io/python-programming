def count_words_starting_with_v(string):
    words = string.split()
    count = 0
    for word in words:
        if word.startswith('v') or word.startswith('V'):
            count += 1
    return count
input_string = "Violet is a vibrant color, very visible in the vast valley."

count_v_words = count_words_starting_with_v(input_string)
print("Number of words starting with 'v':", count_v_words)
