sentence = input("Please enter a sentence: ")

alternating_sentence = ""  # this holds the new sentence that will alternate casing

# this loops over the length of the inputted sentence
for i in range(0, len(sentence)):
    # if the current index is a positive number, then added the current letter to the variable as a capitol letter
    if i % 2 == 0:
        alternating_sentence = alternating_sentence + sentence[i].upper()
    # else add the current letter to the variable as a lowercase letter
    else:
        alternating_sentence = alternating_sentence + sentence[i].lower()

print(str(alternating_sentence))  # print the alternating sentence

# split the sentence into different words
alternating_words = sentence.split(" ")
# create an array to hold the result
alternating_words_result = []
# as the for loop doesn't use an int, we declare one here to keep an index to find out even and odd words
index = 0
for i in alternating_words:
    if index % 2 == 0:
        alternating_words_result.append(i.lower())

    else:
        alternating_words_result.append(i.upper())

    # we need to manually increment this index here
    index += 1

print(alternating_words_result)
