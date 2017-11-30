#/usr/bin/python3
import datetime
import os
import sys
from pprint import pprint as pp

location = os.getcwd() + '/data'
words_movies = dict()
try:
    if len(os.listdir(location)) <= 0:
        sys.exit("The data directory is empty.")
except(FileNotFoundError):
    sys.exit("'data' directory not found on current working directory.")

movie_ids = {key: value for (key, value) in enumerate(os.listdir(location))}

def process():
    """This function process all movie data inside the data directory
    filling an dictionary with an ID for each movie found.
    """
    for k, v in movie_ids.items():
        with open(os.path.join(location, v), 'r') as f:
            words = set(f.readline().strip().split())
            for w in words:
                if w in words_movies:
                    words_movies[w].add(k)
                else:
                    words_movies[w] = set([k])


def main(terms):
    """This function searches for the criteria and if they
    match it's going to be printed in alphabetical order

    terms: string
    """
    if not isinstance(terms, str):
        raise TypeError("Invalid type. Expected {} but got {}".format(type(str), type(terms)))

    terms = terms.split()
    print("\n")

    start = datetime.datetime.now()

    if set(terms).issubset(words_movies.keys()):
        # get the movies for each keyword
        set_list = [words_movies.get(term) for term in terms]
        selected_movies = set(set_list[0]).intersection(*set_list)
        found = [movie_ids[x]
                   for x in selected_movies]  # retrieve movie data
        end = datetime.datetime.now()
        pp(sorted(found))
        print("\nFound {} in {}".format(len(found), (end - start).total_seconds()))
    else:
        end = datetime.datetime.now()
        print("No entries found for the given criteria")
        print("Time spent: {}".format((end-start).total_seconds()))


if __name__ == '__main__':
    try:
        if sys.argv[1] == "":
            sys.exit("Please provide a valid criteria")
    except(IndexError):
        sys.exit("Argument missing, please provide it.")
    print("Processing list...")
    process()
    print("Done. Searching for: '{}'".format(sys.argv[1]))
    main(sys.argv[1])
