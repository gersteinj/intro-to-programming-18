inventory = {
    'apples': 1,
    'bananas': 5,
    'chocolate': 3,
    'durian': 0,
    'eclair': 2
}

# print number of apples
print(inventory['apples'])
# add 2 apples
inventory['apples'] += 2
# print number of apples again
print(inventory['apples'])
# add flour to the inventory
# if flour already existed in dictionary, value would be modified
inventory['flour'] = 5
# print quantity of flour
print(inventory['flour'])