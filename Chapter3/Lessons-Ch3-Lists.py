import time

# Create Lists
empty_list = [ ]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
big_birds = ["emu", "ostrich", "cassowary"]
first_names = ["Graham", "John", "Terry", "Terry", "Michael"]

another_empty_list = list()
print(another_empty_list)

# Convert Other Data Types to Lists with list()
list("cat")
print(list("cat"))

a_tuple = ("ready", "fire", "aim")
list(a_tuple)
print(list(a_tuple))

birthday = "1/6/1952"
birthday_split = birthday.split("/")
print(birthday_split)

splitme = "a/b//c/d///e"
splitme_result = splitme.split("/")
print(splitme_result)

splitme_result_2 = splitme.split("//")
print(splitme_result_2)

# Get an Item by Using [offset]
marxes = ["Groucho", "Chico", "Harpo"]
print(marxes[0])
print(marxes[1])
print(marxes[2])

print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

# error by index
# print(marxes[5])

# Lists of Lists
small_birds = ["hummingbird", "finch"]
extinct_birds = ["dodo", "passenger pigeon", "Norwegian Blue"]
carol_birds = [3, "French hens", 2, "turtledoves"]
all_birds = [small_birds, extinct_birds, "macaw", carol_birds]

print(all_birds)

print(all_birds[0][1])

# Change an Item by [offset]
marxes[2] = "Wanda"
print(marxes)

marxes[2] = "Harpo"

# Get a Slice to Extract Items by Offset Range
print(marxes[0:2])

print(marxes[::2])

print(marxes[::-2])

print(marxes[::-1])

# Add an Item to the End with append()
marxes.append("Zeppo")
print(marxes)

# Combine Lists by Using extend() or +=
others = ["Gummo", "Karl"]

start = time.perf_counter()
marxes.extend(others)
end = time.perf_counter()
print(marxes)
print(f"Elapsed time extend: {end - start:.8f} seconds")

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

start = time.perf_counter()
marxes += others
end = time.perf_counter()
print(marxes)
print(f"Elapsed time +=: {end - start:.8f} seconds")


marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']

start = time.perf_counter()
marxes.append(others)
end = time.perf_counter()
print(marxes)
print(f"Elapsed time append: {end - start:.8f} seconds")

# Add an Item by Offset with insert()
marxes.insert(3, "Gummo")
print(marxes)

marxes.insert(10, "Karl")
print(marxes)

# Delete an Item by Offset with del
del marxes[-1]
print(marxes)

print(marxes[2])
del marxes[2]
print(marxes)
print(marxes[2])

# Delete an Item by Value with remove()
marxes.remove("Gummo")
print(marxes)

# Get an Item by Offset and Delete It by Using pop()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.pop())
print(marxes)

print(marxes.pop(1))
print(marxes)

# Find an Item's Offset by Value with index()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes.index("Chico"))

# Test for a Value with in
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print("Groucho" in marxes)
print("Bob" in marxes)

words = ['a', 'deer', 'a', 'female', 'deer']
print("deer" in words)

# Count Occurrences of a Value by Using count()
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes.count("Harpo"))

print(marxes.count("Bob"))

snl_skit = ["cheeseburguer", "cheeseburguer", "cheeseburguer"]
print(snl_skit.count("cheeseburguer"))

# Convert to a String with join()
marxes = ['Groucho', 'Chico', 'Harpo']
print(", ".join(marxes))

friends = ["Harry", "Hermione", "Ron"]
separator = " * "
joined = separator.join(friends)
print(joined)

separated = joined.split(separator)
print(separated)

# Reorder Items with sort()
marxes = ["Groucho", "Chico", "Harpo"]
sorted_marxes = sorted(marxes)
print(sorted_marxes)

print(marxes)

marxes.sort()
print(marxes)

numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
print(numbers)

# Get Length by Using len()
marxes = ["Groucho", "Chico", "Harpo"]
lengthOfMarxes = len(marxes)
print(lengthOfMarxes)

# Assign with =, Copy with copy()
a = [1, 2, 3]
print(a)

b = a
print(b)

a[0] = "surprise"
print(a)
print(b)

a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = "integer lists are boring"

print(a)
print(b)
print(c)
print(d)