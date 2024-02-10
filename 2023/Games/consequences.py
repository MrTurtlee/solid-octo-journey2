import random

woman = ["a scientist", "a queen", "a pirate", "a giant rabit"]
man = ["a police officr", "an artist", "Your grandfather", "a killer robot"]

place = ["on Pluto.", "at the supermarket.", "in a spooky, bat-filled cave."]
she_wore = ["scuba diving gear.", "fairy wings.", "a paper bag."]
he_wore = ["a purple suit.", "a shark costume.", "a beach towel."]
woman_says = ["'Who are you?'", "'How many beans make five?'", "'why?'"]
man_says = ["'Beep boop!'", "'Dont't eat the frogs'", "'What time do you call this?'"]
consequence = ["'World peace.'", "'chaos'", "'a giant frog squashes them.'", "'rainbows.'"]
world_said = ["'Errant nonsense!'", "'cheese is trending now.'", "'I'm melting!'"]

input("\npress enter to play again\n")

# printing a certain woman meeting a certain man at a place
print(random.choice(woman), "met", random.choice(man), "at", random.choice(place))

# print: "She was wearing", a certain female clothing
print("She was wearing", random.choice(she_wore))

# print: "He was wearing", a certain male clothing
print("He was wearing", random.choice(he_wore))

# print: "She said,", a certain female dialogue
print("She said", random.choice(woman_says))

# print: "He said,", a certain male dialogue
print("He said", random.choice(man_says))

# print: "The consequence was", a certain consequence
print("The consequence was", random.choice(consequence))

# print: "The world said,", a certain world dialouge
print("The world said,", random.choice(world_said))

