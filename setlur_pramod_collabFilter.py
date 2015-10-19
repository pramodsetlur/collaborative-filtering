'''
Algorithm
_________
SETUP
1. Read the input file as a list: input_list
2. Create 2 dictionaries: user_item_dict (key = user, value = dictionary of item and the rating) and user_rating_dict (key = user, value = list[Total ratings for all the movies rated by this user, count of movies rated])
3. Pearson_coeff() - Iterate over user_item_dict and find Pearson Coeff with input_user and the other users: output is a dictionary of [user2, P.C.]. where P.C. is the pearson coeffecient with user2 and the input_user
4. k_nearest_neighbpt() - pick the top k users: output is a list of users which are k nearest
5. predict() - iterate the k nearest neighbors list and output the prediction of the rating for that user.
'''

import sys

def setup_input(input_file):
    input_list = []
    with open(input_file) as file:
        for each_line in file:
            temp_line = each_line.strip().split('\t')
            input_list.append(temp_line)
    file.close()
    return input_list

def collaborative_filter(input_file, user_id, movie_name, k):
    input_list = setup_input(input_file)
    print input_list

if __name__ == '__main__':
    if 5 != len(sys.argv):
        print len(sys.argv)
        print "USAGE: $ python setlur_pramod_collabFilter.py [INPUT_FILE] [USER_ID] [MOVIE_NAME] [K - A number to indicate K nearest neighbors]"
    else:
        input_file = sys.argv[1]
        user_id = sys.argv[2]
        movie_name = sys.argv[3]
        k = sys.argv[4]

        collaborative_filter(input_file, user_id, movie_name, k)