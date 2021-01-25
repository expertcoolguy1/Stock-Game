import random

money = 1000
day = 0
error = 0
want = "yes"



while money >= 0 and want == "yes":
    want = input("do you wish to play again? Enter yes or no ")
    if want == "no":
        print("OK, but you must play one last time")
    error += 1
    while error == 1:
        risk = input("would you like a high, medium, or low risk? ")

        if risk == "low" or risk == "lo" or risk == "Low":
            change_type = random.randint(-50, 50)
            error = 0
            money += change_type

        elif risk == "medium" or risk == "med" or risk == "meduim":
            change_type = random.randint(0, 100)
            error = 0
            money += change_type

        elif risk == "high" or risk == "hi":
            change_type = random.randint(0, 200)
            error = 0
            money += change_type

        else:
            print("ERROR, PLEASE ENTER EITHER HIGH, MEDIUM, OR LOW")
            error = 1


    print("you have $", + money)