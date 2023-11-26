import time

def introduction():
    print("Welcome to the Potato Farmer Adventure!")
    time.sleep(1)
    print("You are a potato farmer in the beautiful state of Idaho. Or maybe Middle Earth? Guess you will find out.")
    time.sleep(1)
    print("Your goal is to make the best decisions to ensure a successful potato farm.")
    time.sleep(1)
    print("Let the adventure begin!\n")

def choose_option(options):
    print("Choose your next move:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def encounter_gollum():
    print("\nAs you wander through the potato fields, you hear a strange noise.")
    time.sleep(1)
    print("You cautiously approach and discover Gollum, the creature from the Lord of the Rings, lurking in your potato farm!")
    time.sleep(1)

    # Decision to deal with Gollum
    print("\nWhat will you do?")
    gollum_options = ["Offer him some potatoes", "Try to scare him away", "Call for help"]
    choice = choose_option(gollum_options)

    if choice == 1:
        print("\nYou offer Gollum some potatoes. Surprisingly, he seems delighted and leaves peacefully, which is surprising because he hates taters.")
        time.sleep(1)
    elif choice == 2:
        print("\nYou attempt to scare Gollum away, but he becomes agitated and causes a little chaos in the potato fields.")
        time.sleep(1)
        print("Unfortunately, your attempt to scare Gollum attracts the attention of a more sinister presence.")
        return "lose"
    elif choice == 3:
        print("\nYou call for help, and nearby farmers come to assist in removing Gollum from your farm.")
        time.sleep(1)

def encounter_sauron():
    print("\nOne evening, as the sun sets, a dark shadow falls upon your farm.")
    time.sleep(1)
    print("Sauron, the Dark Lord from the Lord of the Rings, appears with his menacing presence.")
    time.sleep(1)

    # Decision to deal with Sauron
    print("\nWhat will you do?")
    sauron_options = ["Confront Sauron bravely", "Seek magical help", "Flee and hide"]
    choice = choose_option(sauron_options)

    if choice == 1:
        print("\nYou confront Sauron bravely, but his power overwhelms you. The game is lost.")
        return "lose"
    elif choice == 2:
        print("\nYou seek magical help, and the powerful wizard Gandalf the White appears to banish Sauron from your farm.")
        time.sleep(1)
    elif choice == 3:
        print("\nYou flee and hide, narrowly escaping Sauron's wrath.")
        time.sleep(1)

def seek_shane():
    print("\nYou hear rumors about Shane, a legendary farmer known for his expertise.")
    time.sleep(1)
    print("Shane is said to be in a nearby town. Would you like to seek his help?")
    shane_options = ["Yes, seek Shane's help", "No, handle the challenges on your own"]
    choice = choose_option(shane_options)

    if choice == 1:
        print("\nYou decide to seek Shane's help. He arrives at your farm, ready to assist in any challenges.")
        time.sleep(1)
    elif choice == 2:
        print("\nYou choose to handle the challenges on your own. It's a brave decision!")
        time.sleep(1)

def visit_market():
    print("\nYou decide to visit the local market to buy supplies for your farm.")
    time.sleep(1)
    print("At the market, you meet Samwise, a friendly farmer selling fresh produce.")
    time.sleep(1)

    # Decision at the market
    print("\nWhat will you do?")
    market_options = ["Buy potatoes from Samwise", "Trade crops with other farmers", "Skip the market and return to the farm"]
    choice = choose_option(market_options)

    if choice == 1:
        print("\nYou buy some potatoes from Samwise, supporting her business and ensuring a variety in your crops.")
        time.sleep(1)
    elif choice == 2:
        print("\nYou decide to trade some of your crops with other farmers, fostering good relationships in the community.")
        time.sleep(1)
    elif choice == 3:
        print("\nYou skip the market and head back to the farm to focus on your tasks for the day.")
        time.sleep(1)

def new_day_options(day):
    print(f"\nIt's a new day on the potato farm. What will you prioritize today?")
    time.sleep(1)

    # Decision 1 for the new day
    print("\nDecision 1: What should you do first?")
    decision_1_options = [
        "Check the health of the potato plants",
        "Expand your farm infrastructure",
        "Visit a neighboring farm for advice",
        "Participate in a farming competition",
        "Take a day off and relax"
    ]
    choice = choose_option(decision_1_options)

    if choice == 1:
        print("\nYou check the health of the potato plants, ensuring they are thriving and free from diseases.")
        time.sleep(1)
    elif choice == 2:
        print("\nYou decide to expand your farm infrastructure, adding new facilities to improve efficiency.")
        time.sleep(1)
    elif choice == 3:
        print("\nYou visit a neighboring farm and gather valuable advice from experienced farmers.")
        time.sleep(1)
    elif choice == 4:
        print("\nYou participate in a farming competition, showcasing your skills and learning from others.")
        time.sleep(1)
    elif choice == 5:
        print("\nYou take a day off to relax and recharge, enjoying the tranquility of your farm.")
        time.sleep(1)

    # Decision 2 for the new day
    print("\nDecision 2: What's your next move?")
    decision_2_options = [
        "Experiment with new potato varieties",
        "Upgrade your farming equipment",
        "Host a community event at your farm",
        "Explore a mysterious part of your land",
        "Collaborate with neighboring farmers"
    ]
    choice = choose_option(decision_2_options)

    if choice == 1:
        print("\nYou experiment with new potato varieties, hoping to discover a unique and valuable crop.")
        time.sleep(1)
    elif choice == 2:
        print("\nYou upgrade your farming equipment, increasing productivity and efficiency.")
        time.sleep(1)
    elif choice == 3:
        print("\nYou host a community event at your farm, strengthening bonds with your neighbors.")
        time.sleep(1)

# Run the adventure
introduction()
days = 1

while days <= 3:
    if days > 1:
        print(f"\nCongratulations! You've completed Day {days - 1} on the potato farm.")
    new_day_options(days)

    # Increment the day counter
    days += 1

    # Encounter Gollum after the first day
    if days == 2:
        result = encounter_gollum()
        if result == "lose":
            print("Unfortunately, your adventure as a potato farmer ends here. Better luck next time!")
            break

    # Encounter Sauron after the second day
    if days == 3:
        result = encounter_sauron()
        if result == "lose":
            print("Unfortunately, your adventure as a potato farmer ends here. Better luck next time!")
            break

    print(f"\nYou are starting Day {days} on the potato farm.")
    time.sleep(1)
