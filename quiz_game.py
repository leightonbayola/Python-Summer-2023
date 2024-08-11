print("Welcome to my computer quiz!")

#asks user if they want to play a computer quiz
playing = input("Do you want to play ? ")

#.lower() converts all user input to lowercase so that no matter what case the user inputs if it says for example "YeS" it will still evaluate to true
if playing.lower() != "yes":
    print("Ok, I hope to see you soon! Goodbye!")
    quit()

print("Okay! Let's play :) ")
score = 0

#question #1
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else: print('sorry that is incorrect!')

#question #2
answer = input("What company does AZURE belong to? ")
if answer.lower() == "microsoft":
    print('Correct!')
    score += 1
else: print('sorry that is incorrect!')

#Question #3
answer = input("Who is a famous cofounder of Microsoft? ")
if answer.lower() == "bill gates" or "paul allen":
    print('Correct!')
    score += 1
else: print('sorry that is incorrect!')

#Question #4
answer = input("Who is the current CFO of Microsoft? ")
if answer.lower() == "amy hood":
    print('Correct!')
    score += 1
else: print('sorry that is incorrect!')


print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/4) * 100) + "%.") 

