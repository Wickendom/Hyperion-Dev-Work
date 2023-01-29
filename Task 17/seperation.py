sentence = input("Please input a sentence: ")

separated_sentence = sentence.split()  #this splits the above sentence by creating a list of each word that is seperated by a space

for i in range(0, len(separated_sentence)):  # this loops through each word in the seperated sentence
    print(f"{separated_sentence[i]}")  # this prints the individual word
