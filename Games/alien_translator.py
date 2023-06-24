
alien_dictionary = {
    "we": "vorag",
    "come": "thang",
    "in": "zon",
    "peace": "argh",
    "hello": "kodar",
    "can": "znak",
    "i": "az",
    "borrow": "liftit", 
    "some": "zum", 
    "rocket": "upgoman", 
    "fuel": "kakboom", 
    "please": "slepin", 
    "don't": "baaaaaaaaaarn", 
    "shoot": "flabil", "welcome": "unkip", 
    "our": "mandig", 
    "new": "brang", 
    "alien": "marangin", 
    "overlords": "bap"
}


# Extra challenge:
# I want to add the word: "like" with the alien word: "wefrgf" into
# the dictionary. Can you code this
alien_dictionary["like"] = "wefrgf"


# code logic:

english = input("Type in an english phrase\n")
english = english.split()

alien_words = []
for word in english:
    if (word in alien_dictionary):
        alien_words.append(alien_dictionary[word])
    else:
        # add english word into alien_words instead
        alien_words.append(word)

# .join() join every item in a list together into 1 string
alien_sentance = " ".join(alien_words)

# prints out: "Translation: ", (the actual alien sentance)
print("Translation:",alien_sentance)