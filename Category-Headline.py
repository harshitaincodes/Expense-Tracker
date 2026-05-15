import random

categories = {
    "bollywood" : {

        "subjects" : ["Shahrukh Khan", "Salman Khan", "Katrina Kaif", "Shahid Kapoor", "Ishaan Khatter", "Bobby Deol"],
        "actions" : ["dances with", "launches", "eats"],
        "places": ["at Red Fort", "during award show", "inside movie set"]
    },

    "sports": {
        "subjects": ["Virat Kohli", "Rohit Sharma", "MS Dhoni"],
        "actions": ["wins", "throws", "celebrates with"],
        "places": ["during IPL", "at Wankhede Stadium", "inside dressing room"]
    },

    "politics": {
        "subjects": ["Modi", "Pappu", "A Local MLA"],
        "actions": ["announces", "cancels", "declares"],
        "places": ["inside Parliament", "at India Gate", "during election rally"]
    },

    "funny": {
        "subjects": ["Five Cats", "A Group of Monkeys", "Auto Rickshaw Driver"],
        "actions": ["orders", "steals", "celebrates with"],
        "places": ["a plate of Samosa", "at metro station", "inside shopping mall"]
    }

}

print("==== Fake Headline Generator ====\n")

print("1. Use Existing Category")
print("2. Add Custom Headline Content")

choice = input("\nEnter your choice (1 or 2): ").strip()

if choice == "1":

    print("Available Categories: ")
    for category in categories:
        print("-",category)



    chosen_category = input("Choose a category: ").strip().lower()
    if chosen_category in categories:
        data = categories[chosen_category]

    else:
        print("Invalid category selected!")
        exit()   

elif choice == "2":
    user_subject = input("Enter a custom subject name: ")
    user_action = input("Enter a custom action: ")
    user_place = input("Enter a custom place or thing: ")

    data = {
        "subjects": [user_subject],
        "actions": [user_action],
        "places": [user_place]
    }

else:
    print("Invalid choice!")
    exit()    

while True:
        subject = random.choice(data["subjects"])    
        action = random.choice(data["actions"])    
        place = random.choice(data["places"]) 

        headline = f"BREAKING NEWS: {subject} {action} {place}"
        print("\n" + headline)

        save = input("\nDo you want to save this headline to a file (yes/no)").strip().lower()

        if save == "yes":
            with open("headlines.txt", "a") as file:
                file.write(headline + "\n")

            print("Headline saved Successfully!")
        

        user_input = input("\nDo you want another headline (yes/no): ").strip().lower()

        if user_input == "no":
            break

else:
    print("Invalid Category Selected!")

print("\nThanks for using Fake Headline Generator!")    