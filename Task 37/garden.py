import spacy #This statement should work if you have spaCy installed

gardenpathSentances = [
    "After the young Londoner had visited his parents prepared to celebrate their anniversary",
    "Time flies like an arrow; fruit flies like a banana",
    "Mary gave the child the dog bit a Band-Aid",
    "I know the words to that song about the queen don’t rhyme.",
    "Helen is expecting tomorrow to be a bad day"
]

nlp = spacy.load('en_core_web_sm')

for sentence in gardenpathSentances:
    doc = nlp(sentence)
    doc.text.split()
    # Tokenize each word in the current sentence
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    # print a label that is found in the current sentence by using entity recognition
    print([(i, i.label_, i.label) for i in doc.ents])

print(spacy.explain("DATE"))
print(spacy.explain("PERSON"))

# i used DATE and PERSON for this, the first was DATE which was picked up by the term 'tomorrow' which makes
# sense as it means the next day. The next i picked was PERSON which was picked up by the token 'MARY'
# which makes sense as it is a persons name. i was unable to find a label that i did not understand