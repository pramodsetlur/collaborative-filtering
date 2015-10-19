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

def update_user_rating_dict(each_line, user_rating_dict):
    user = each_line[0]
    rating = each_line[1]
    item = each_line[2]

    user_rating_dict.setdefault(user, [0, 0])
    temp_list = user_rating_dict[user]
    temp_list[0] += float(rating)
    temp_list[1] += 1
    user_rating_dict[user] = temp_list

    return user_rating_dict

def update_user_item_dict(each_line, user_item_dict):
    user = each_line[0]
    rating = float(each_line[1])
    item = each_line[2]

    user_item_dict.setdefault(user, {})
    temp_dict = user_item_dict.get(user)
    temp_dict.setdefault(item, rating)
    user_item_dict[user] = temp_dict

    return user_item_dict


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

    user_item_dict = {}
    user_rating_dict = {}

    for each_line in input_list:
        user_item_dict = update_user_item_dict(each_line, user_item_dict)
        user_rating_dict = update_user_rating_dict(each_line, user_rating_dict)

    generate_pearson_coeff_list(user_item_dict, user_rating_dict)


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