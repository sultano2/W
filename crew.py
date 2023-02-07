HamptonCrewbies = ["Sultan","Anh","Jack","Queen","Brenna","Jobe","Logan","Maggie","Medly","Sammy","Hampton","Faith","Kalid","Stephanie","Marwa","Liam"]
correct = []
guess = []
tries = 16
length = len(HamptonCrewbies)
while len(HamptonCrewbies) > 0 and tries > 0:
    userInput = input("please enter the name of a crewbie:")
    if HamptonCrewbies.count(userInput) > 0:
        print ("Crewbie is on the list! Who else?")
        HamptonCrewbies.remove(userInput)
        correct.append(userInput)
    elif HamptonCrewbies.count(userInput) == 0:
        tries = 1
        print ("Person is not in the crew")
while len(HamptonCrewbies) <= 0:
    print ("you win")
    break
