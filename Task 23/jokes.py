import random

# create a list of jokes
list_of_jokes = [
    "What’s the best thing about Switzerland?   - I don’t know, but the flag is a big plus.",
    "I invented a new word!   - Plagiarism!",
    "Did you hear about the mathematician who’s afraid of negative numbers?   - He’ll stop at nothing to avoid them."
]
# print a random joke by getting a random number between 0 and the length of the joke array
print(list_of_jokes[random.randint(0,len(list_of_jokes))])