lst = ["a", "b", "a", "c", "b", "a"]

# 1. Write Python code to count how many times each element appears in a list.

count = {}              # create an empty dictionary to store counts

for x in lst:           # go through each item in the list one by one
    if x in count:      # if the item is already in the dictionary
        count[x] += 1   # increase its count by 1
    else:               # if the item is not in the dictionary
        count[x] = 1    # add it with count 1

count

# or 

from collections import Counter

Counter(lst)





# 2. Write Python code to find the second largest number in a list.
# using sort

lst = [10, 20, 4, 45, 99]

lst.sort()              # sort the list
second_largest = lst[-2] # second last element
print(second_largest)


lst.sort(reverse = True)
second_largest = lst[1]
second_largest




# 3. Write Python code to remove duplicates from a list but keep the original order.

lst = [1, 2, 2, 3, 4, 3, 5]   

unique = []                  # empty list to store unique items

for x in lst:                # go through each item in the list
    if x not in unique:      # check if the item is not already added
        unique.append(x)     # add the item for the first time

print(unique)                # show the list without duplicates





# 5. Write Python code to check if a string is a palindrome (same forward and backward).

text = "madam"
if text == text[::-1]:      # check if string equals its reverse
    print('palindrome')
else:
    print('not_palindrome')


rev = ""
for x in text:             # reverse string manually
    rev = x + rev

if text == rev:
    print('palindrome')
else:
    print('not_palindrome')

