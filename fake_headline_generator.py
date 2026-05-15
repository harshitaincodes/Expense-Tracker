import random

subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Five Cats",
    "Modi",
    "Pappu",
    "A Group of Monkeys",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "dances with",
    "eats",
    "cancels",
    "celebrates",
    "declares war with",
    "orders"
]

places_or_things = [
    "at Red Fort",
    "Mumbai Local Train",
    "inside Parliament",
    "during IPL",
    "at India Gate",
    "at Ganga Ghat",
    "a plate of Samosa"
]


while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing} "
    print("\n" + headline)

    #save headline to a file
    save = input("\nDo you want to save this headline to a file. (yes/no)").strip().lower()

    if save == "yes":
        with open("headlines.txt", "a") as file:
            file.write(headline + "\n")

        print("Headline saved Successfully!")


    user_input = input("\nDo you want another healine? (yes/no)").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using fake headline generator ")