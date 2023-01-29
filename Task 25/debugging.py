def print_values_of(dictionary, keys):
    for key in keys:
        # changed k to key to use the variable in the for loop
        print(dictionary[key])


# I changed the d'oh to use speech marks which stops the string from formatting incorrectly
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh", "maggie": " (Pacifier Suck)"}

# i added square brackets where the keys are in the below line to create an array of keys
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

