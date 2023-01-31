#In the exercise below, use the given lists to print out a set containing all the participants from event A which did not attend event B.
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
for i in a:
    if i not in b:
        print(i)