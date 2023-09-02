def my_name(name):
    print(f"my name is {name}")
my_name("shahad")
def my_meal(food,drink):
    print(f"I like to eat {food} and while drinking {drink}")
my_meal("apple","water")
def cube(number):
    return number**3
def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
result = by_three(9)
print(result)

    
    