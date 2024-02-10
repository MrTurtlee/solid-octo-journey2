import random


def beau_fav_anime(anime):
    print("Beau's' Favourite anime is", random.choice(anime))

def harry_fav_anime(anime):
    print("Harry's Favourite anime is", random.choice(anime) )
    beau_fav_anime(anime)

def main():
    anime = ["One piece", "Naruto", "Bleach", "Black Clover", "Dragon Ball"]
    
    random.choice(anime)

    harry_fav_anime(anime)

main()