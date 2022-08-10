# set
my_set = {1, 2, 3}
print(my_set)

# only unique items are in
my_set = {1, 2, 2, 3, 4, 4}
print(my_set)

# list casts to set
my_list = [1, 2, 3, 4, 4, 5, 5]
my_set = set(my_list)
print(my_set)

# add one item
my_set.add(6)
print(my_set)

# add more items
my_set.update([7, 8, 9])
print(my_set)

# discard / remove item
my_set.discard(10) # no item but no error
my_set.remove(99) # no item with error!!!
print(my_set)