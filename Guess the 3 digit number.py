import random


def all_unique(x):
   seen = set()
   return not any(a in seen or seen.add(a) for a in x)


numbers = random.sample(range(1, 10), 3)
if all_unique(numbers):
    print(numbers)
else:
    numbers = random.sample(range(1, 10), 3)

lst = list(map(int, input(
        "Enter the integer elements of list: ")))[:3]

if all_unique(lst):
    print('The list is:', lst)   # printing the list
    if lst == numbers:
        print("that's correct")

    def common_member(numbers, lst):
        set_numbers = set(numbers)
        set_lst = set(lst)

        if len(set_numbers.intersection(set_lst)) > 0:
            return set_numbers.intersection(set_lst)
        else:
            print("no common elements")


    while lst != numbers:
        print(len(common_member(numbers, lst)), "number(s) in common")
        lst = list(map(int, input(
            "I guess it's: ")))[:3]
        if all_unique(lst):
            print('The list is:', lst)
            if lst == numbers:
                print("that's correct")

else:
    print('pick unique numbers')