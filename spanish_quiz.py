''' Zero Nelson 
February 9, 2025
Project 1 
Spanish Quiz 

This program is a Spanish vocabulary test where the user is asked five questions about common Spanish words.
For each question, the user has two chances to answer correctly, with points awarded based on which attempt is correct. 
After all questions, the program displays the user's final score and offers encouragement based on success. 

Create variables to store data required later in program
Get input from user 5 times 
Include at least 5 conditional statements (at least 3 elif)
'''

print("\n" + "*" * 45)
print("             Spanish Vocab Test      ")
print("*" * 45 + "\n")

print("\n⭐  1 point if correct on first try")
print("⭐ .5 point if correct on second try")
print("\nYou only have two chances to gain points, good luck!")

score = 0

answer = input("\nWhat is the word for 'Day'? ").lower()
if answer == 'dia':
    print("\nQue bueno!")
    score += 1
else:
    answer = input("\nOh no, try again... \n\nEnter here: ").lower()
    if answer == 'dia':
        print("\nQue bueno!")
        score += .5
    else:
        print("\nMaybe next time!")

answer = input("\nWhat is the verb for 'to end'? ").lower()
if answer == 'terminar':
    print("\nQue bueno!")
    score += 1
elif answer == 'acabar':
    print("\nQue bueno!")
    score += 1
else: 
    answer = input("\nOh no, try again... \n\nEnter here: ").lower()
    if answer in ['acabar','terminar']:
        print("\nQue bueno!")
        score += .5
    else:
        print("\nMaybe next time!")

answer = input("\nWhat is the adjective for 'long'? ").lower()
if answer == 'largo':
    print("\nQue bueno!")
    score += 1
else:
    answer = input("\nOh no, try again... \n\nEnter here: ").lower()
    if answer == 'largo':
        print("\nQue bueno!")
        score += .5
    else:
        print("\nMaybe next time!")

answer = input("\nWhat is one verb for 'to be'? ").lower()
if answer == 'ser':
    print("\nQue bueno!")
    score += 1
elif answer == 'estar':
    print("\nQue bueno!")
    score += 1
else:
    answer = input("\nOh no, try again... \n\nEnter here: ").lower()
    if answer in ['estar', 'ser']:
        print("\nQue bueno!")
        score += .5
    else:
        print("\nMaybe next time!")

answer = input("\nWhat is one verb for 'to know'? ").lower()
if answer == 'conocer':
    print("\nQue bueno!")
    score += 1
elif answer == 'saber':
    print("\nQue bueno!")
    score += 1
else:
    answer = input("\nOh no, try again... \n\nEnter here: ").lower()
    if answer in ['saber', 'conocer']:
        print("\nQue bueno!")
        score += .5
    else:
        print("\nMaybe next time!")

if score == 5:
    print(f"\nExcellent job! You've earned a perfect score of {score}/5")
elif score > 0:
    print(f"\nGreat job! You've earned a score of {score}/5")
else:
    print(f"\nPractice more and come back later! You've earned a score of {score}/5")