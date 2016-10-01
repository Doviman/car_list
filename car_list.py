cars =[]
newcar = ""

print "Please list types of cars, and when finished type done"
while newcar != "done":
    newcar = raw_input("Please enter a type of car: ")
    if newcar != "done":
        cars.append(newcar)


cars.sort()
for vette in cars:
    print vette




