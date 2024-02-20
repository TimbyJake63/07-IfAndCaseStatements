###############################################################################
# DONE: 1. (3 pts)
#
#   Write a function called color_picker() that prints out a message to a user.
#
#   This function should do the following:
#     1. Prompt the user to enter the name of a color.
#     2. Using case statements, if it matches the color that they picked, it should print out a success message like so:
#           "Success! You picked red."
#        Do NOT use f-strings here. Just use regular strings and use the case statement to pick which string to print.
#     3. You should have a case for at least 5 colors of your choosing.
#     3. If the user picks a color that you do not have a case for, it should print:
#           "Unknown Color!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def color_picker():
    txt = input("Enter Color: ")
    match txt:
        case "red":
            print("Gotta love red")
        case "blue":
            print("Let's goooooooo, best color no question")
        case "green":
            print("ok ok I like it I guess, it's not too bad")
        case "yellow":
            print("What a horrible choice")
        case "purple":
            print("just fun to ykyk")
        case _:
            print("Prolly forgot to put in that color or you're just stupid and didn't read the question")

###############################################################################
# DONE: 2. (3 pts)
#
#   Write a function called grade() that tells a student what letter grade they
#   got on an assignment based on the percentage they indicate.
#
#   This function should do the following:
#     1. Prompt the user to enter a percentage. They should enter the
#        percentage as a decimal (so an 85% should be entered as 0.85)
#     2. Using case statements, check which range the percentage is in and print a statement telling the user what grade they got on the assignment. It should look something like:
#           "You received a(n) A."
#     3. Your ranges should match a standard grading scale where greater than or equal to 90% is an A, etc.
#     4. If the user enters an invalid percentage, the function should print:
#           "Invalid Score!"
#
#   Make sure you call your function to start things off.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
def grade():
    grade=float (input("Enter percentage for assignment in decimal form (i.e. .85 for 85%): "))
    match grade:
        case _ if 0.9 <= grade <=1.0:
            print("You got an A!")
        case _ if 0.8 <= grade <0.9:
            print("You got a B!")
        case _ if 0.7 <= grade <0.8:
            print("You got an C!")
        case _ if 0.6 <= grade <0.7:
            print("You got an D!")
        case _ if 0.0 <= grade <0.6:
            print("You got an F, Failure haha!")
        case _:
            print("Invalid Score!")
grade()
            

