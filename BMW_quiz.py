print("Welcome to my game about BMW!")

name = input("What's your name? ")
age = input("How old are you? ")

print("Hi, ", name.capitalize()," you are ", age," years old.")


if int(age) >= 18:
    print("You are allowed to play")
    
    wants_to_play = input("Do you want to play? (yes/no) ").lower()
    if wants_to_play == "yes":
        print("Cool, let's play!!!")
        live = 5
        points = 0
        print("You are starting with", live, "lives")
        
        question1 = input("1. Which of the following models does not belong to BMW? \nA. 1600 \nB. Z8 \nC. 2001C \n").upper()
        if question1 == "C" or question1 == "2001C":
            print("Correct!\n")
            points += 1
        else:
            live -= 1
            print("Incorrect. Lost 1 live")
            print("Now you have ", live, " lives!\n")
            if live == 0:
                print("Game Over!")
            
        question2 = input("2. What is the horsepower of the BMW 740i model? \nA. 215 \nB. 315 \nC. 415 \n").upper()
        if question2 == "B" or question2 == "315":
            print("Correct!\n")
            points += 1
        else:
            live -= 1
            print("Incorrect. Lost 1 live")
            print("Now you have ", live, " lives!\n")
            if live == 0:
                print("Game Over!")
            
        question3 = input("3. Which luxury car brand was acquired by BMW in 1998? \nA. Jaguar \nB. Bentley \nC. Rolls-Royce \n").upper()
        if question3 == "C" or question3 == "Rolls-Royce":
            print("Correct!\n")
            points += 1
        else:
            live -= 1
            print("Incorrect. Lost 1 live")
            print("Now you have ", live, " lives!\n")
            if live == 0:
                print("Game Over!")
            
        question4 = input("4. The headquarter of BMW is located in which German city? \nA. Frankfurt am Main \nB. Munich \nC. Stuttgart \n").upper()
        if question4 == "B" or question4 == "Munich":
            print("Correct!\n")
            points += 1
        else:
            live -= 1
            print("Incorrect. Lost 1 live")
            print("Now you have ", live, " lives!\n")
            if live == 0:
                print("Game Over!")
            
        question5 = input("5. In which year was BMW founded? \nA. 1906 \nB. 1916 \nC. 1926 \n").upper()
        if question5 == "B" or question5 == "1916":
            print("Correct!\n")
            points += 1
        else:
            live -= 1
            print("Incorrect. Lost 1 live")
            print("Now you have ", live, " lives!\n")
            if live == 0:
                print("Game Over!")
        #Total Score
        score = float(points / 5) * 100
        print(points,"out of 5, that is",score, "%")
            
    else:
        print("That's sad! See you next time")
else:
    print("Sorry, you are too young!")           