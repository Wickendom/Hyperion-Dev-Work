word = input("Please input a word")

# declare a dictionary of the letters that occur in the word
word_to_evaluate = {}

for char in word:
    # adds the character occurrence into the dictionary
    word_to_evaluate.update({char:0})

for char in word:  # loop over each character in the string
    word_to_evaluate[char] += 1  # add to the value of the character found

print(word_to_evaluate)  # print the dictionary