people_for_dinner = ["tuna", "trout", "pompano"]

print("Hello " + people_for_dinner[0] + ", you are invited for dinner")
print("Hello " + people_for_dinner[1] + ", you are invited for dinner")
print("Hello " + people_for_dinner[2] + ", you are invited for dinner")
print("\n")

print(people_for_dinner[1] + " is not coming for dinner")
print("\n")
people_for_dinner[1] = "salmon"
print("Hello " + people_for_dinner[0] + ", you are invited for dinner")
print("Hello " + people_for_dinner[1] + ", you are invited for dinner")
print("Hello " + people_for_dinner[2] + ", you are invited for dinner")
print("\n")
print("I have got a bigger table with three people space availabe")
people_for_dinner.insert(0, "permit")
people_for_dinner.insert(2, "geany")
people_for_dinner.append("tykal")

print("\n")
print("Hello " + people_for_dinner[0] + ", you are invited for dinner")
print("Hello " + people_for_dinner[1] + ", you are invited for dinner")
print("Hello " + people_for_dinner[2] + ", you are invited for dinner")
print("Hello " + people_for_dinner[3] + ", you are invited for dinner")
print("Hello " + people_for_dinner[4] + ", you are invited for dinner")
print("Hello " + people_for_dinner[5] + ", you are invited for dinner")

print("\n")

print("Your table cant arrive on time, you can invite only two people for dinner.")
print("\n")
popped_person = people_for_dinner.pop()
print("Sorry  " + popped_person + ", I cannot invite you to dinner")
popped_person = people_for_dinner.pop()
print("Sorry  " + popped_person + ", I cannot invite you to dinner")
popped_person = people_for_dinner.pop()
print("Sorry  " + popped_person + ", I cannot invite you to dinner")
popped_person = people_for_dinner.pop()
print("Sorry  " + popped_person + ", I cannot invite you to dinner")

print("\n")

print("Hello " + people_for_dinner[0] + ", you are still invited for dinner")
print("Hello " + people_for_dinner[1] + ", you are still invited for dinner")

del people_for_dinner[1]
del people_for_dinner[0]

print("\n")
print(people_for_dinner)
