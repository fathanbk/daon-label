import math

numbers = [2.7, 2.9, 3.2, 3.4]
category = ['small number', 'big number']
    
# make range number into category dynamically
def make_range(numbers, category):
    # find max and min number
    max_number = max(numbers)
    min_number = min(numbers)

    # find range
    range_number = max_number - min_number

    # find range for each categor
    range_category = range_number / len(category)

    cat_range = []
    for i in range(len(category)):
        cat_range.append(min_number + (range_category * (i+1)))
    
    # make range
    range_list = []
    for i in range(len(category)):
        if i == 0:
            range_list.append([min_number, cat_range[i]])
        elif i == len(category)-1:
            range_list.append([cat_range[i-1], max_number])
        else:
            range_list.append([cat_range[i-1], cat_range[i]])

    return range_list

ranges = make_range(numbers, category)
range1 = ranges[0]
for i in range(int(range1[0]), int(range1[1]+1)):
    print(i)
print(make_range(numbers, category))