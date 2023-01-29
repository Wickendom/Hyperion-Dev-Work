sentence = input("Please enter a sentence: ")
strip_characters = input("Please enter the letters you would like to remove from the previous sentence: ")  # this asks the users what characters want to be removed

for i in range(0, len(strip_characters)):  #loop over the below code an amount of times equal to the amount of characters the user wants to remove
    sentence = sentence.replace(strip_characters[i], "")  #this finds the characters in the sentence using the current index of characters to remove and removes them

print(sentence)  #print the stripped sentence