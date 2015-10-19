# Collaborative Filtering
USAGE: setlur_pramod_collabFilter.py [INPUT_FILE]  [USER_ID] [ITEM_NAME] [K - A number to indicate K nearest neighbors]

This program takes an input file which contains a list of ratings given by many users to many items (or movies)
But some users may have not given a rating for an item. I predict the user rating for an item using:

Pearson Coeffecient: To find out similar users to the input username

k-nearest-neighbor: To find out the k-nearest neighbors or users

Weighted average: To predict the user rating for an item given in the input based on Peason coeffecients and the k-nearest neighbors

Link for reference: https://web.stanford.edu/class/cs246/slides/07-recsys1.pdf
