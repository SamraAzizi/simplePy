print("welcome to computer quiz ")
playing = input("Do you want to play quiz: ")

if playing.lower() != 'yes':
    quit()

print("Ok! let's play ")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    print("Correct!")
    score += 1
    print("well done you can move to the next question")

else:
    print("Incorrect!")
    print("Its Ok! next question")


answer = input("What does GPU stand for? ")
if answer.lower() == 'graphic processing unit':
    print("Correct!")
    score += 1
    print("well done you can move to the next question")

else:
    print("Incorrect!")
    print("Its Ok! next question")



answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    print("Correct!")
    score += 1
    print("well done you can move to the next question")

else:
    print("Incorrect!")
    print("Its Ok! next question")




answer = input("What does SPU stand for? ")
if answer.lower() == 'supply power':
    print("Correct!")
    score += 1
    print("well done you can move to the next question")

else:
    print("Incorrect!")
    print("Its Ok! next question")




answer = input("What does ISP stand for? ")
if answer == 'internet service provider':
    print("Correct!")
    score += 1
    print("well done you can move to the next question")

else:
    print("Incorrect!")
    print("Its Ok! next question")


print("you got "+str(score)+" questions correct")
print(f"you got {(score/5) *100}%.")
###############################################


#guessing number game 
import random
from xml.etree.ElementTree import TreeBuilder

num = input("enter a number: ")

if num.isdigit():
    num = int(num)

    if num <= 0:
        print("pleas enter a number greater than 0!")
        quit()
else:

    print("enter a number for next ")
    quit()
      


random_num = random.randint(0,num)
guesses = 0

while True:
    guesses += 1

    guess_num = input("guess the number ")

    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print("enter a number for next ")
        continue

    if guess_num == random_num:
        print("wow you got it! ")
        break
    
    elif guess_num > random_num:
        print("you were above the random number")
    else:
        print("you were below the random number")

print("you got ", guesses, "guesses")



###############################


import random

userwin = 0
compwin = 0
options = ["rock","paper","scissor"]
while True:
    userinput = input("choose ROCK/PAPER/SCISSOR or Q to quit: ").lower()
    if userinput == 'q':
        break

    if userinput not in options:
        continue

    randomnum = random.randint(0,2)
    # 0: rock  1:paper  2:scissors
    comppick = options[randomnum]
    print("computer picked ", comppick)

    if userinput == 'rock' and comppick == 'scissor':
        print("you won!")
        userwin += 1
       

    elif userinput == 'paper' and comppick == 'rock':
        print("you won!")
        userwin += 1
       


    elif userinput == 'scissor' and comppick == 'paper':
        print("you won!")
        userwin += 1
    else:
        print("you lost , computer won")
        compwin += 1

print("you won ", userwin, "times.")
print("computer won ", compwin, "times.")

print("goodbye!")

###############################################

####ADVENTURE GAME////////////////

name = input("Type your name: ")
print("welcome to game",name)

answer = input("you are on a dirt road you need to go left or right choose your way? ").lower()

if answer == 'left':
    answer2 = input("now you are on a river would you like to walk or swim type walk to walk around and swim to swim across? ").lower()
    if answer2 == 'walk':
        print("you walked for a  miles and you are tired and ran out of water you lose!")
    
    elif answer2 =='swim':
        print("you swam across and you are eaten by an alligator and you lose!")

    else:
        print("not a valid option , you lose!")

elif answer == 'right':
    answer3 = input("you are on a bridge, it looks wobbly would you like to cross the bridge ot head back:(cross/back):  ").lower()

    if answer3 == 'back':
        print("you chose to go back, you lose!")
    
    elif answer3 =='cross':
        answer4 = input("you chose to cross the bridge, now you meet a person you wanna talk (yes/no) :").lower()

        if answer4 == 'yes':
            print("you talked to a stranger and they gave you gold you WIN!")

        elif answer4 == 'no':
            print("you ignored the stranger you lose!")

        else:
            print("not a vlid option , you lose!")

    else:
        print("not a valid option , you lose!")


else:
    print("not a valid option, you lose!")


print("thank you for trying ", name)





import tkinter as tk

calculation = ""

def add(symbol):
    global calculation
    calculation += str(symbol)
    text_r.delete(1.0, "end")
    text_r.insert(1.0,calculation)
    

def sub():

    global calculation
    try:

        calculation = str(eval(calculation))
        
        text_r.delete(1.0, "end")
        text_r.insert(1.0, calculation)
    except:
        clear()
        text_r.insert(1.0, "Error")
        

    

def clear():
    global calculation
    calculation = ""
    text_r.delete(1.0, "end")
    

root = tk.Tk()
root.geometry("300x270")

text_r = tk.Text(root, height = 2, width = 16, font= ("Arial", 24))
text_r.grid(columnspan = 5)

btn1 = tk.Button(root, text="1", command= lambda:add(1), font=("Arial", 14), width = 6)
btn1.grid(row=2, column = 1)

btn2 = tk.Button(root, text="1", command= lambda:add(2), font=("Arial", 14), width = 6)
btn2.grid(row=2, column = 2)

btn3 = tk.Button(root, text="3", command= lambda:add(3), font=("Arial", 14), width = 6)
btn3.grid(row=2, column = 3)


btn4 = tk.Button(root, text="4", command= lambda:add(4), font=("Arial", 14), width = 6)
btn4.grid(row=3, column = 1)


btn5 = tk.Button(root, text="5", command= lambda:add(5), font=("Arial", 14), width = 6)
btn5.grid(row=3, column = 2)


btn6 = tk.Button(root, text="1", command= lambda:add(6), font=("Arial", 14), width = 6)
btn6.grid(row=3, column = 3)


btn7 = tk.Button(root, text="7", command= lambda:add(7), font=("Arial", 14), width = 6)
btn7.grid(row=4, column = 1)


btn8 = tk.Button(root, text="8", command= lambda:add(8), font=("Arial", 14), width = 6)
btn8.grid(row=4, column = 2)


btn9 = tk.Button(root, text="9", command= lambda:add(9), font=("Arial", 14), width = 6)
btn9.grid(row=4, column = 3)

btn0 = tk.Button(root, text="0", command= lambda:add(0), font=("Arial", 14), width = 6)
btn0.grid(row=5, column = 2)

btnP = tk.Button(root, text="+", command= lambda:add("+"), font=("Arial", 14), width = 6)
btnP.grid(row=2, column = 4)


btnM = tk.Button(root, text="-", command= lambda:add("-"), font=("Arial", 14), width = 6)
btnM.grid(row=3, column = 4)


btnMU = tk.Button(root, text="*", command= lambda:add("*"), font=("Arial", 14), width = 6)
btnMU.grid(row=4, column = 4)


btnD = tk.Button(root, text="/", command= lambda:add("/"), font=("Arial", 14), width = 6)
btnD.grid(row=5, column = 4)


btnopen = tk.Button(root, text="(", command= lambda:add("("), font=("Arial", 14), width = 6)
btnopen.grid(row=5, column = 1)


btnclose = tk.Button(root, text=")", command= lambda:add(")"), font=("Arial", 14), width = 6)
btnclose.grid(row=5, column = 3)


btnEq = tk.Button(root, text="=", command=sub, font=("Arial", 14), width = 11)
btnEq.grid(row=6, column = 3, columnspan= 2)

btnclear = tk.Button(root, text="C", command=clear, font=("Arial", 14), width = 11)
btnclear.grid(row=6, column = 1, columnspan= 2)


root.mainloop()


#///////////////////////////////////////////////////////////////////