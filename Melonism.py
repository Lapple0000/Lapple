    #Melonism faith tester
ques_ans = 0 #count how many questions were answered to give a percentage grade
prayer = "Dear Melons, I shall love you from birth to death, from one corner of the world to the other, I hope you will bring grace to my life, I will not let the pumpkins do anything to my children or my wife, Melon" 
#This is the prayer the user needs to recite in question 4
correct = 0
incorrect = 0 #correct and incorrect counter, duh
ques_result = []
c_count = 0 # this is to count how many times the user has selected the option to give the sum of 1+1
import random #this was just in case
import time
print('Warning: This does not actually test your faith.\nIf you are actually faithful to Melonism, seek help.\nMelonism is a joke.\n')

def again(): #the menu after you do the quiz
    global ques_result
    global c_count
    while True:
        end = input("Would you like to do?\n A. Play again\n B. Show me what questions I got wrong\n C. Give me the sum of 1+1\n D. Stop playing\n")
        if end.lower() == 'a': #play again
            print("Great, let's play!\n")
            break
        
        elif end.lower() == 'b': #results
            print('\nOkay! Here are the results:\n')
            time.sleep(3)
            num = 1
            for i in ques_result:
                if num == 4:
                    num += 1
                    continue
                print(f'You got question {num} {i}!\n')
                num += 1
                time.sleep(2)
            print("And for number 4...\n")
            time.sleep(2)
            print("...\n")
            time.sleep(2)
            if ques_result[3] == 'wrong':
                print("YOU GOT IT WRONG BOZO OH MY GOD HOW COULD YOU MESS UP THAT PRAYER??!!!\n")
                time.sleep(2)
            elif ques_result[3] == 'right':
                print("You got it right!\n")
                time.sleep(2)
            elif ques_result[3] == 'Ultra Skibidi Deluxe':
                print("Holy tuff boi. Like 67 Tung Tung Tung Sahur kinda tuff. Skibidi.\n")
                time.sleep(2)
                    
        elif end.lower() == 'c': #1+1=2
            if c_count < 12:
                print ('\n2\n')
                time.sleep(2)
                c_count += 1
            elif c_count < 24:
                print("\nBro, it's 2\n")
                c_count += 1
                time.sleep(2)
            else:
                print('STOP IT!!')
                time.sleep(2)
                print("Nah i'm done")
                time.sleep(2)
                quit("too many 2")
                
        elif end.lower() == 'd': #quit
            print("Okay then, I see how it is\n")
            time.sleep(2)
            quit()
            
        elif end == "Are you a different animal and the same beast?":
            kobe = input("\nWhat does that mean Kobe Bryant?\n")
            if kobe == "You're welcome":
                while True:
                    print("Kanye West")
            else:
                print("You are not Tung Tung Tung Sacool :disapointed_emoji:")
                time.sleep(2)
                quit()
        else:
            print("\nThat's not a real answer.\n")
            time.sleep(2)

while True: # the game logic that I managed to make work on a single while loop. Probably not the best thing
    def ques1(): #defines questions
        global ques_ans
        ques_ans += 1
        while True:
            ans = input("Who created the peaceful world?\n A. Melons\n B. Pumpkins\n").lower()
            
            if ans == "a":
                global correct
                correct += 1
                return "right"
            
            elif ans == "b":
                global incorrect
                incorrect += 1
                return "wrong"
            
            else: #choosing an answer thats not there won't count it wrong
                print("\nThat's not an option, please select a or b\n")
                
    def ques2(): #ditto
        global ques_ans
        ques_ans += 1
        while True:
            ans = input("\nWho brought evil into the world?\n A. Melons\n B. Pumpkins\n").lower()
            
            if ans == "b":
                global correct
                correct += 1
                return "right"
            
            elif ans == "a":
                global incorrect
                incorrect += 1
                return "wrong"
            
            elif ans == "lebron james":
                quit()
            
            else:
                print("\nThat's not an option, please select a or b\n")
                
    def ques3(): #ditto
        while True:
            global ques_ans
            ques_ans += 1
            ans = input("\nAccording to the Book of Melon, what mob's fossils can you find in the nether?\nA. Blaze\nB. Creeper\nC. Ghast\nD. Enderman\n").lower()
            
            global incorrect
            global correct
            
            if ans == "b":
                incorrect += 1
                return "wrong"
            
            elif ans == "a":
                incorrect += 1
                return "wrong"
            
            elif ans == "c":
                correct += 1
                return "right"
            
            elif ans == "d":
                incorrect += 1
                return "wrong"
            
            elif ans == "kanye west":
                quit()
            
            else:
                print("\nThat's not an option, please select a, b, c, or d\n")        
    
    def ques4(): # open answe question, so 1 typo is wrong
        global ques_ans
        ques_ans += 1
        ans = input ("\nRecite this prayer:\nDear Melons, I shall love you from birth to death,\nfrom one corner of the world to the other,\nI hope you will bring grace to my life,\nI will not let the pumpkins\ndo anything to my children or my wife,\nMelon\n")
        global prayer
        global correct
        global incorrect
        
        if ans == prayer:
            time.sleep(2)
            print("\nGood Job\n")
            correct += 1
            return "right"
            time.sleep(2)
            
        elif ans == "skibidi toilet": 
            correct += 78626536578947656787654345678746567465356273643567387645367654637
            return "Ultra Skibidi Deluxe"
            
        elif ans.lower() == "kanye west":
            quit()
            
        elif ans.lower() == "lebron james":
            quit ()
        
        elif ans.lower() == "triple t":
            print ("tung tung tung " * 8)
            time.sleep(10)
            quit()
        
        else:
            time.sleep(2)
            print('\nShameful\n')
            return "wrong"
            incorrect += 1
            time.sleep(2)
    def ques5(): # ditto
        global ques_ans
        global incorrect
        global correct
        ques_ans += 1
        while True:
            ans = input("Who were the Pumpkins first targets?\n A. Villagers\n B. The Undead\n C. Melons\n D. Pigs\n").lower()
            if ans == "a":
                incorrect += 1
                return "wrong"
            elif ans == "b":
                correct += 1
                return "right"
            elif ans == "c":
                incorrect += 1
                return "wrong"
            elif ans == 'd':
                incorrect += 1
                return 'wrong'
            elif ans== "where is omni-man":
                for i in range(67):
                    print('WHERE IS HE?!')
                quit('WHERE IS HE?!')
            
            else:
                print("\nThat is not an option, please select a, b, c, or d")
            
    def ques6():# ditto
        global correct
        global incorrect
        global ques_ans
        ques_ans += 1
        while True:
            ans = input("\nHow did the Pumpkins enter despite the farland walls?\n A. Villagers let them through\n B. They didn't\n C. They phased through the walls \n D. They slowly destroyed the walls\n").lower()
            
            if ans == "a":
                incorrect += 1
                return "wrong"
            
            elif ans == "b":
                incorrect += 1
                return "wrong"
            
            elif ans == 'c':
                incorrect += 1
                return "wrong"
            
            elif ans == "d":
                correct += 1
                return 'right'
            
            else:
                print("\nNot an option.\n")
                
                
                
    ques_result.append(ques1()) #actually calls up the questions and uses the results for option B in the post-quiz menu
    ques_result.append(ques2())
    ques_result.append(ques3())
    ques_result.append(ques4())
    ques_result.append(ques5())
    ques_result.append(ques6())
    perc = int((correct / ques_ans) * 100) # gives percentage grade
    time.sleep(2)
    print(f"\nYou are {perc}% faithful\n")
    time.sleep(2)
    if perc < 50: #messages depending on grade
        print("You are genuinely such a failure\n")
        time.sleep(2)
    elif perc < 70:
        print('Do better')
        time.sleep(2)
    elif perc < 80:
        print('Average')
        time.sleep(2)
    elif perc < 100:
        print('Almost there\n')
        time.sleep(2)
    elif perc == 100:
        print("You are a true child of Melonism")
        time.sleep(2)
    else:
        print('CITY BOIIIIIIIIIIIIIII SKIBIDI TUFF TUNG TUNG TUNG') #yes
        time.sleep(2)
    correct = 0 #resets these variables so you can play again
    incorrect = 0
    ques_ans = 0
    again() #calls up the post-quiz menu
    ques_result = []#comes after the post_quiz menu in order for option B to work