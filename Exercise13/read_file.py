print("This code uses the open and read methods to slurp the entire contents of pelican.txt")
lines = open("pelican.txt").read()
(type(lines))
print("The data is returned as a string.")
print(lines)
print("---")
print("This code uses the readlines method to turn the file into a list and prints the number of items in that list")
lineslist = open("pelican.txt").readlines()
print(len(lineslist))
print("---")
print("This method uses a loop to iterate over the contents of the file. Adding the end parameter prevents extra new lines being added.")
#why don't we need a file object here?
for line in open("pelican.txt"):
    print(line, end = "")
print("---")
#why doesn't close work?



