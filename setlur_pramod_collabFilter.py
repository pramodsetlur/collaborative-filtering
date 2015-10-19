'''
Algorithm
_________

'''

import sys

def collaborative_filter(input_file, user_id, movie_name, k):
    print "test"

if __name__ == '__main__':
    if 4 != len(sys.argv):
        print "USAGE: $ python setlur_pramod_collabFilter.py [INPUT_FILE] [USER_ID] [MOVIE_NAME] [K - A number to indicate K nearest neighbors]"
    else:
        input_file = sys.argv[1]
        user_id = sys.argv[2]
        movie_name = sys.argv[3]
        k = sys.argv[4]

        collaborative_filter(input_file, user_id, movie_name, k)