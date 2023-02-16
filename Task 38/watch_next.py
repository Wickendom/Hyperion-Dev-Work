import spacy

nlp = spacy.load('en_core_web_md')

def get_similar_movie(film_description):
    similar_movie = ""
    similar_score = 0
    film_desc_to_check = nlp(film_description)

    #iterate over each movie and find the most similar movie and then return it
    for line in movies:
        desc = nlp(line)
        similarity = desc.similarity(film_desc_to_check)

        if similarity > similar_score:
            similar_movie = line
            similar_score = similarity

    return similar_movie

# reads the movie file
movies_file = open("movies.txt", "r")

# gets a list of the movies
movies = movies_file.readlines()
# print the most similar movie by calling the get_similar_movie function using a films description
print(get_similar_movie("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to aplanet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."))