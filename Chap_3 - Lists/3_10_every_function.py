animals = ["goat", "cow", "camel", "buffalo"]
print(animals)

# modify or change item
animals[-1] = "monkey"
print(animals)

# insert item
animals.insert(0, "horse")
animals.insert(2, "giraffe")
animals.insert(3, "gorilla")
print(animals)

# append item
animals.append("tiger")
animals.append("leopard")
animals.append("dog")
print(animals)

# remove by index
del animals[3]
print(animals)

# remove by value
animals.remove("monkey")
print(animals)

# pop item in a variable
popped_animal = animals.pop()
print(animals)
print(popped_animal)
popped_animal = animals.pop(5)
print(animals)
print(popped_animal)


# sort temporily
print(sorted(animals))
print(animals)

# sort permanently
animals.sort()
print(animals)

# reverse the order
animals.reverse()
print(animals)

# len of items in a list

print(len(animals))
