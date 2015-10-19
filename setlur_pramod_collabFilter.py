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
import math

def predict(user_id, item_name, k_nearest_neighbors_list):
    

def k_nearest_neighbors(pearson_coeffecient_list, k):
    k_nearest_neighbors_list = []
    sorted_k_nearest_neighbors_list = sorted(pearson_coeffecient_list.items(), key = lambda x:x[1])

    count = 0
    for i in reversed(sorted_k_nearest_neighbors_list):
        if count < k:
            k_nearest_neighbors_list.append(i)
            count += 1
    return k_nearest_neighbors_list

def calculate_avg_rating(user, user_rating_dict):
    temp_list = user_rating_dict[user]
    total_rating = temp_list[0]
    count = temp_list[1]

    average = total_rating / count
    return average


def pearson_correlation(user1, user2, user_item_dict, user_rating_dict):
    user1_items = user_item_dict[user1]
    user2_items = user_item_dict[user2]
    user1_avg_rating = calculate_avg_rating(user1, user_rating_dict)
    user2_avg_rating = calculate_avg_rating(user2, user_rating_dict)

    numerator = 0
    denominator_pt1 = 0
    denominator_pt2 = 0

    for item, rating in user1_items.iteritems():
        if item in user2_items:
            user1_item_rating = user_item_dict.get(user1).get(item)
            user2_item_rating = user_item_dict.get(user2).get(item)

            numerator += (user1_item_rating - user1_avg_rating) * (user2_item_rating - user2_avg_rating)
            denominator_pt1 += (user1_item_rating - user1_avg_rating) * (user1_item_rating - user1_avg_rating)
            denominator_pt2 += (user2_item_rating - user2_avg_rating) * (user2_item_rating - user2_avg_rating)

    denominator = math.sqrt(denominator_pt1) * math.sqrt(denominator_pt2)
    pearson_coeffecient = numerator / denominator

    return  pearson_coeffecient

def generate_pearson_coeff_list(user1, user_item_dict, user_rating_dict):
    pearson_coeffecient_dict = {}
    for user2, items in user_item_dict.iteritems():
        if user1 != user2:
            pearson_coeffecient = pearson_correlation(user1, user2, user_item_dict, user_rating_dict)
            pearson_coeffecient_dict.setdefault(user2, pearson_coeffecient)

    return  pearson_coeffecient_dict

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

def collaborative_filter(input_file, user_id, item_name, k):
    input_list = setup_input(input_file)

    user_item_dict = {}
    user_rating_dict = {}

    for each_line in input_list:
        user_item_dict = update_user_item_dict(each_line, user_item_dict)
        user_rating_dict = update_user_rating_dict(each_line, user_rating_dict)

    pearson_coeffecient_list = generate_pearson_coeff_list(user_id, user_item_dict, user_rating_dict)
    k_nearest_neighbors_list = k_nearest_neighbors(pearson_coeffecient_list, k)
    predicted_rating = predict(user_id, item_name, k_nearest_neighbors_list)


if __name__ == '__main__':
    if 5 != len(sys.argv):
        print len(sys.argv)
        print "USAGE: $ python setlur_pramod_collabFilter.py [INPUT_FILE] [USER_ID] [ITEM_NAME] [K - A number to indicate K nearest neighbors]"
    else:
        input_file = sys.argv[1]
        user_id = sys.argv[2]
        item_name = sys.argv[3]
        k = int(sys.argv[4])

        collaborative_filter(input_file, user_id, item_name, k)