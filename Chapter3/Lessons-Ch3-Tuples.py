# Tuples
# Are immutables

empty_tuple = ()
print(empty_tuple)

one_marx = "Groucho",
print(one_marx)

marx_tuple = "Groucho", "Chico", "Harpo"
print(marx_tuple)

# Tuple unpacking
marx_tuple = ("Groucho", "Chico", "Harpo")
a, b, c = marx_tuple
print(a)
print(b)
print(c)

password = "swordfish"
icecream = "tuttifrutti"
password, icecream = icecream, password
print(password)
print(icecream)

marx_list = ["Groucho", "Chico", "Harpo"]
new_tuple = tuple(marx_list)
print(new_tuple)

