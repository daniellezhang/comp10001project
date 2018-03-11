'''project description:
The service you will implement is a simple Restaurant Finder Service. 
We will use many simplifying assumptions in this project to make life easier.
We will work on the simple 2-dimensional Cartesian coordinate system,
using Euclidean distances to simplify our world.
You will build the core functionality for our LBS for the city of Gridbourne. 
The city of Gridbourne has 100 neighbourhoods, each cell in this grid is a 
neighbourhood and has a name. The name is created using a simple 
mechanism as described below. Note that there are exactly 100 cells, 
and the naming of the cells follow this 10×10 layout;
i.e., A1 to A10 on the first row, B1 to B10 on the second row, 
and so on up until J1 to J10. Not all names are shown in the figure above for 
the brevity of the example.
'''

'''code to generate coordinate for every restaurant
and calculate their distance to the given coordinate'''

from itertools import product
from math import sqrt

# dictionaries to map the coordinates to the name of the neighbourhood
X_COORDINATE = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7',
                7: '8', 8: '9', 9: '10'}
Y_COORDINATE = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G',
                7: 'H', 8: 'I', 9: 'J'}
# corner restaurants' coordinates
COORDINATE_VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
corner_restaurant = product(COORDINATE_VALUES, COORDINATE_VALUES)
corner_restaurant_lst = [c for c in corner_restaurant]
complete_restaurant_lst = corner_restaurant_lst + []
# coordninates of restaurants in the middle of the neighbourhood
for i in corner_restaurant_lst:
    x = i[0] + 0.5
    y = i[1] + 0.5
    complete_restaurant_lst.append((x, y))


def restaurant_distance(x, y):
    '''find the distances of all restaurants to the given coordinates'''
    # a list that store the name of the restaurant and its distance
    distance_lst = []
    for restaurant in complete_restaurant_lst:
        # calculate the distance to the restaurant
        distance = sqrt((x - restaurant[0]) ** 2 + (y - restaurant[1]) ** 2)
        # the name of the neighbourhood the restaurant is in
        name = Y_COORDINATE[restaurant[1] // 1] +\
            X_COORDINATE[restaurant[0] // 1]
        # determine the name of the restaurant
        if restaurant[0] % 1 == 0:
            name += 'CR'
        else:
            name += 'MR'
        distance_lst.append((distance, name))
    # sort the list in the order of distance
    return sorted(distance_lst)


def find_restaurants_to_shut(distance, list_of_epicentres):
    '''find all the restaurants within the given distance to the epicentres and
    return it in a list of list'''

    all_restaurants_to_shut_lst = []
    for epicentre in list_of_epicentres:
        # calculate every restaurant's distance to the epicentre
        restaurant_distance_to_epicentre_lst \
            = restaurant_distance(epicentre[0], epicentre[1])
        restaurants_to_shut_lst = []
        # find restaurants that are strictly less than the given distance
        # to a single epicentre
        for restaurant in restaurant_distance_to_epicentre_lst:
            if restaurant[0] >= distance:
                break
            else:
                restaurants_to_shut_lst.append(restaurant[1])
        all_restaurants_to_shut_lst.append(sorted(restaurants_to_shut_lst))
    
    return all_restaurants_to_shut_lst


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_restaurants_to_shut(1.0, [[3.0, 3.0]]))
    print(find_restaurants_to_shut(0.4, [[1.0, 1.0], [2.0, 2.0]]))
