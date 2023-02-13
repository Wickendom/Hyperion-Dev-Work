def add_prefix_un(word):
    return f"un{word}"


def make_word_groups(vocab_words):
    new_words = []
    # loops over each word and adds that with the prefix to the above array
    for i in range(1, len(vocab_words)):
        new_words.append(f"{vocab_words[0]}{vocab_words[i]}")

    return_string = f"{vocab_words[0]}"

    # formats the words into a readable string
    for word in new_words:
        return_string += f" :: {word}"

    return return_string


def remove_suffix_ness(word):
    new_word = word
    # gets the last 4 characters of the given string and checks if it is 'ness'
    split_word = word[-4:]
    if split_word == "ness":
        # if it is, remove the last 4. then check if the word ends with an 'i'. if it does replace it with a 'y'
        new_word = new_word[:-4]
        if new_word[-1:] == "i":
            new_word = new_word[:-1]
            new_word += "y"
            return new_word
        else:
            return new_word
    else:
        print(f"{word} does not end with 'ness'")


def adjective_to_verb(sentence, index):
    split_sentence = sentence.split(" ")
    # adds the prefix to the word at the given index
    split_sentence[index] += "en"

    joined_sentence = ""
    # joins the words back together including a space
    for word in split_sentence:
        joined_sentence += f"{word} "

    return joined_sentence


print(add_prefix_un("happy"))
print(make_word_groups(["en", "close", "joy", "lighten"]))
print(remove_suffix_ness("happiness"))
print(adjective_to_verb('I need to make that bright', -1))