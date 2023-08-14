# Creating an array of dictionaries representing objects
objects = [
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Accessing the dictionaries (objects) directly
# first_object = objects[0]
second_object = objects[1]
third_object = objects[2]

# Accessing attributes of individual objects
print("Title:", objects[0]["title"])
print("Author:", objects[0]["author"])
print()

print("Title:", second_object["title"])
print("Author:", second_object["author"])
print()

print("Title:", third_object["title"])
print("Author:", third_object["author"])
print()

# # Accessing the dictionaries and their attributes
# for obj in objects:
#     print("Title:", obj["title"])
#     print("Author:", obj["author"])
#     print()
