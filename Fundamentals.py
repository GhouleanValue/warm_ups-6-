# Another assortment of exercises for Python beginners

#1 | Minimum and maximum

mylist = [12,23,34,45,56,67,78,89,90]

#for the minimum in a list use
print(min(mylist))

#for the maximum in a list use
print(max(mylist))

#2 | Lets use min and max in a for loop

items = [1,2,3,4,5,6,7,8,9]

for num in items:
    print(max(list(items)))
           # replace max with min and see what happens


#3 | zip function

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item)


#4 | More of the range function

#converting a range of numbers ca be quicker than creating a log list.

#instead of listing 1, 100 in a list we can use the below range and add list to the front.

#I have done this before in previouse exercises but I think it is useful to reiterate.

range(1, 100)

new_list = list(range(1, 100))

print(new_list)

#5 | Lets use it one more time in a slightly larger way

my_list = list(range(1,100))

even = 0
odd = 0

for item in my_list:
    if item % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'amount of even numbers {even}')
print(f'amount of odd numbers are {odd}')
