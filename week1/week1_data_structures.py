#### LIST ####
print("__________________LIST__________________", end="\n\n")
num = [10,20,30,40]
names = [ "kapil", "rahul", "amit"]

print(num)
print(names)

print(num[0])
print(names[-1])

num.append(50)
print(num)

num.remove(20)
print(num)


#### TUPLES ####
print("__________________TUPLES__________________", end="\n\n")
point = (10,20)
user = ("kapil", 30, "india")
print(point)
print(user)

print(point[0])
print(user[1])

# Uncommenting below line will cause error
# user[0] = "rahul" # TypeError

config = ("localhost", 5432, "postgres")
print(config)


#### SETS ####
print("__________________SETS__________________", end="\n\n")
number_set = {10,20,30,30,40}
print(number_set)

number_set.add(50)
number_set.add(50) # unique elm, so this will not work now
print(number_set)

number_set.add("jj")
print(number_set)

number_set.remove("jj")
print(number_set)

# Membership check
print(30 in number_set)
print(60 in number_set)

#mini task
emails = ["a@gmail.com","b@gmail.com","k@gmail.com","a@gmail.com","b@gmail.com"]
unique_emails = set(emails)
print(emails, unique_emails, sep="\n")


#### DICTIONARIES ####
print("__________________DICTIONARIES__________________", end="\n\n")
user = {
    "name"      : "kapil",
    "age"       : 29,
    "country"   : "India",
}

print(user)

print(user['name'])
print(user['age'])

user['country'] = "London"
user['age'] = 30
print(user)

user.pop('age')
print(user)

product = {
    "id"        : 1,
    "name"      : "Protine Powder",
    "price"     : 5400,
    "in_stock"  : True
}
print(product['id'])
print(product['name'])
print(product['price'])
print(product.get("in_stock", False))
print(product.get("in_stockkkk", "default-value"))



print("__________________END__________________", end="\n")
print('''
# Week 1 - Conclusion
# List  → ordered collection
# Tuple → fixed record
# Set   → unique items
# Dict  → structured data''', 
end="\n\n")

# Week 1 
# List  → ordered collection
# Tuple → fixed record
# Set   → unique items
# Dict  → structured data
