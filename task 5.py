def most_frequent(string):
    freq_dict = {}
    for letter in string:
        if letter.isalpha():
            freq_dict[letter] = freq_dict.get(letter, 0) + 1
            sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
            for item in sorted_freq:
                print(f"{item[0]}: {item[1]}")
most_frequent("mississippi")
