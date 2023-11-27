def function1 (a,b):
    print(a)
    return a+b
print(function1(5,7))
function1(9,2)
tab = [5,"5"]
new_person = {'name': 'John',
              'age': 38,
              'weight': 160.2,
              'has_glasses': False}
print(new_person['name'])
print(len(new_person))  
import random
print(random.randint(2,5)) # provides a random number between 2 and 5
name = "Zen"
print("My name is", name, tab)
name = "Zen"
print("My name is " + name +tab[1])

def test_fun(x):
    if x>10:
        return "over 10"
    else:
        return "under 10"
print(test_fun(5))

