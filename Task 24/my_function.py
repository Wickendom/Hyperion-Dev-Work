def days_of_the_week():
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")


def replace_words_with_hello(sentence):
    # split the sentence
    split_sentence = sentence.split(" ")
    new_split_sentence = ""
    index = 0
    for word in split_sentence:
        if index % 2 == 1:  # if the current index is an odd number, then add the word hellow to the result
            new_split_sentence += " Hello"
        else:  # else add the word in the inputted sentence instead
            new_split_sentence += f" {split_sentence[index]}"
        index += 1
    print(new_split_sentence)

# calls the days of the week function
days_of_the_week()
# calls the replace words function with the hello function
replace_words_with_hello(input("Please enter a sentence "))
