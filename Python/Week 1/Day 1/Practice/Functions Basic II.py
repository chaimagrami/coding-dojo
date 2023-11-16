# countdown 

def countdown(number):
    return list(range(number, -1, -1))



# print and return 

def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]

# first plus length
def first_plus_length(list):
    return list[0] + len(list)


# values greater than second

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    
    second_value = lst[1]
    new_list = []
    
    print(len(new_list))
    return new_list

# this length, that value

def this_length_that_value(size, value):
    return [value] * size

