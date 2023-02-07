#HamptonCrewbies = ["Sultan","Anh","Jack"]
#for crewbie in HamptonCrewbies:
#    print(crewbie)
#    print("this line is inside the loop.")
# print("looooooooooooooooooooooooooooooooooooooong")



for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
