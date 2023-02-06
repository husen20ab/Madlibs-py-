# # string concatination

# youtuber = "Husen "


# print("subscribe to " + youtuber) # common
# print("subscribe to {}".format(youtuber)) # using .format
# print(f"subscribe to {youtuber}") # f-string

# will use f-strting for the madlibs

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
person = input("person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {person}";

print(madlib)