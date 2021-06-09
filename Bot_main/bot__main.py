import datetime
import webbrowser
import os
import wikipedia
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Data_Base = open ("Data_Base.txt","a") #This is database 

#These are Keywords
hi = ("hi", "hello",)
youtub = ("YouTube", "yt", "youtube")
tim = ("time", "tim")
quitin = ("/quit", "quit")
me = ("whoami", "who am i")
mail = ("mail", "message")
hdln = ("headline", "headlines", "hdln", "news")
Cov19 = ("covid-19", "covid", "covid 19", "corona", "virus")
whoru = ("who are you", "whoareyou", "whoareu", "are you", "whats your name", "what is hour name","name")
month = ("month", "per month")
day = ("day today", "day")
date = "date"
year = "year"
srch = "google"
wiki = ("wiki", "wikipedia")
maths = ("addition", "add", "sum", "subtract", "minus",
         "maths", "multiply", "divide", "calculate", "devide","maths")
face_recog = ("FaceRecognition", "facerecognition",
              "facerecog", "face recognition")
howru = ("how are you","are you fine","are you good","are you sad","hows your mood","howru")
whos = ("who is","whos")


all = (hi,youtub,tim,quitin,me,mail,hdln,Cov19,whoru,month,day,date,year,srch,wiki,maths,face_recog,howru,whos)

hour = int(datetime.datetime.now().hour)
minutes = int(datetime.datetime.now().minute)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def Data_Write():
    Data_Base.write("\n \n \n \n")
    Data_Base.write(f"Function executed Now: \n hour: {hour} , minutes: {minutes}")
    print("Starting")



def welcome():
    print("Hello!")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def WishMe():
    if hour >= 0 and hour < 12:
        print("Good Morning!")
       
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
      
    else:
        print("Good Evening!")
        

    print("how may I help you")


#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def main():

    user_input = input("Type: ").lower()
    Data_Base.write(f"UserInput : ({user_input}) \n")

    user_words = user_input.split()
    Data_Base.write(f"UserWords : ({user_words})\n")

    


    for word in user_words:

        if word in hi: 
            print("Hello")
            Data_Base.write(f"hello executed, [{word}]\n  \n")
            return main()

        elif word in quitin:
            print("Okay Goodbye")
            Data_Base.write(f"quit executed , [{word}] , TOQ ({hour}:{minutes})\n  \n")

        elif word in youtub:
            print("Opening Youtube")
            webbrowser.open_new_tab('https://www.youtube.com')
            Data_Base.write(f"Youtube executed , [{word}] \n \n")
            return main()

        elif word in tim:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"The time is {strTime}(in 24 hour clock)")
            
            Data_Base.write(f"time executed , [{word}] \n \n")
            return main()

        elif word in me:
            print("You are Ishan my founder")
            Data_Base.write(f"me executed , [{word}] \n \n")
            return main()

        elif word in mail:
            print("Opening Mail")
            webbrowser.open_new_tab('https://mail.google.com/mail/u/0/#inbox')
            Data_Base.write(f"mail executed , [{word}] \n \n")
            return main()

 
        elif word in hdln:
            print("Showing Headlines ")
    
            webbrowser.open_new_tab(
                'https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
            Data_Base.write(f"headline executed , [{word}] \n \n")
            return main()

        elif word in Cov19:
            print("Showing Status of covid 19 ")
            webbrowser.open_new_tab(
                'https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=en-IN&gl=IN&ceid=IN%3Aen')
            Data_Base.write(f"Cov19 executed , [{word}] \n \n")
            return main()

        elif user_input == "who are you":
            print("I am a virtual assistant")
            Data_Base.write(f"who are you executed \n \n")
            return main()

        elif word in whoru:
            print("My name is Test I am a Virtual Assistant, My work is to help you ")
            Data_Base.write(f"whoru executed , [{word}] \n \n")
            return main()

        elif word in month:
            x = datetime.datetime.now()
            print(x.strftime("%B"))
            
            Data_Base.write(f"month executed , [{word}] \n  \n")
            return main()

        elif word in day:
            y = datetime.datetime.now()
            print(y.strftime("%A"))
            
            Data_Base.write(f"day executed , [{word}] \n \n")
            return main()

        elif word in date:
            z = datetime.datetime.now()
            print(z.strftime("%D"))
           
            Data_Base.write(f"date executed , [{word}] \n \n ")
            return main()

        elif word in year:
            a = datetime.datetime.now()
            print(a.strftime("%Y"))
            
            Data_Base.write(f"year executed , [{word}] \n \n")
            return main()

        elif word in srch:
            asker = input("what do you want to search: ")
            print(asker)
            
            webbrowser.open(f"https://www.google.com/search?q={(asker)}")
            print("searching on google")
            
            Data_Base.write(f"srch executed , [{word}] \n \n")
            return main()

        elif word in wiki:
            ques = input("what do you want to search on wikipedia:")

            print("what do you want to search on wikipedia:")
            
            print(f"searching {(ques)} on wikipedia")
           
           
            print("*This is what I found*")

            result = wikipedia.summary(ques, sentences=4)
            print(result)
           
            Data_Base.write(f"wikipedia executed , [{word}] , result ({result}) \n \n")
            return main()

        elif word in face_recog:
            path = ("Desktop/FaceReconitiong_Python/Main_FaceRecog/Face_multi.py")
            os.system(f"open {path}")
            
            print(
                "Now Code of Face Recognition will be activated, Run it to do Face Recognition")
            Data_Base.write(f"face_recog executed , [{word}] \n \n")
            return main()

        elif word in maths:
            Data_Base.write(f"Maths executed , [{word}] \n \n")
            return maths_solver()

        elif word in howru or word == "how are you":
            print("I dont know, I cant feel I am here just to help you out of your problems")
            Data_Base.write(f"howru executed , [{word}] \n \n")
            return main()
        
        elif word in whos:
            print("workin on it")
            Data_Base.write(f"whos executed , [{word}] \n \n")
            return main()



        else:
            print("sorry!")
            print("Sorry!")
            Data_Base.write(f"\n \n \n Your Input = [ {user_input} ] , after splitting  -- [ {user_words} ], what I processed -- [ {word} ] \n \n \n")
            return main()


#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def plus():

    Data_Base.write(f"addition executed  \n")

    two = ("2")
    three = ("3")
    four = ("4")

    user_input = input("How many numbers do you want to add ? (max 4) : ")
    user_words = user_input.split()

    for word in user_words:
        if word in two:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("calculating....")

            answer = float(num1)+float(num2)

            print(f"So, {(num1)} + {(num2)} = {(answer)}")
            print(f"So, {(num1)} + {(num2)} = {(answer)}")
            return main()

        if word in three:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")
            print("calculating....")

            answer = float(num1)+float(num2)+float(num3)

            print(f"So, {(num1)} + {(num2)} + {(num3)} = {(answer)}")
            print(f"So, {(num1)} + {(num2)} + {(num3)}= {(answer)}")
            return main()

        if word in four:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")

            print("Enter number 4")
            num4 = input("Enter Number_4:")
            answer = float(num1)+float(num2)+float(num3)+float(num4)
            print("calculating....")

            print(f"So, {(num1)} + {(num2)} + {(num3)} + {(num4)}= {(answer)}")
            print(
                f"So, {(num1)} + {(num2)} + {(num3)} + {(num4)}= {(answer)}")

            return main()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def division():
    print("Enter number 1")
    num1 = input("Enter Number_1:")

    print("Enter number 2")
    num2 = input("Enter Number_2:")

    print("calculating....")

    answer = float(num1) / float(num2)

    print(f"So, {(num1)} / {(num2)} = {(answer)}")
    return main()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


def subtract():
    two = ("2")
    three = ("3")
    four = ("4")

    user_input = input("How many numbers do you want to subtract ? (max 4) : ")
    user_words = user_input.split()

    for word in user_words:

        if word in two:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("calculating....")

            answer = float(num1)-float(num2)

            print(f"So, {(num1)} - {(num2)} = {(answer)}")
            print(f"So, {(num1)} minus {(num2)} = {(answer)}")
            return main()

        if word in three:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")
            print("calculating....")

            answer = float(num1)-float(num2)-float(num3)

            print(f"So, {(num1)} - {(num2)} - {(num3)} = {(answer)}")
            print(
                f"So, {(num1)} minus {(num2)} minus {(num3)}= {(answer)}")
            return main()

        if word in four:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")

            print("Enter number 4")
            num4 = input("Enter Number_4:")
            answer = float(num1)-float(num2)-float(num3)-float(num4)
            print("calculating....")

            print(f"So, {(num1)} - {(num2)} - {(num3)} - {(num4)} = {(answer)}")
            print(
                f"So, {(num1)} minus {(num2)} minus {(num3)} minus {(num4)}= {(answer)}")

            return main()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def multiplication():
    two = ("2")
    three = ("3")
    four = ("4")

    user_input = input("How many numbers do you want to add ? (max 4) : ")
    user_words = user_input.split()

    for word in user_words:
        if word in two:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("calculating....")

            answer = float(num1)*float(num2)

            print(f"So, {(num1)} * {(num2)} = {(answer)}")
            print(f"So, {(num1)} * {(num2)} = {(answer)}")
            return main()

        if word in three:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")
            print("calculating....")

            answer = float(num1)*float(num2)*float(num3)

            print(f"So, {(num1)} * {(num2)} * {(num3)} = {(answer)}")
            print(f"So, {(num1)} * {(num2)} * {(num3)}= {(answer)}")
            return main()

        if word in four:
            print("Enter number 1")
            num1 = input("Enter Number_1:")

            print("Enter number 2")
            num2 = input("Enter Number_2:")

            print("Enter number 3")
            num3 = input("Enter Number_3:")

            print("Enter number 4")
            num4 = input("Enter Number_4:")
            answer = float(num1)*float(num2)*float(num3)*float(num4)
            print("calculating....")

            print(f"So, {(num1)} * {(num2)} * {(num3)} * {(num4)}= {(answer)}")
            print(
                f"So, {(num1)} * {(num2)} * {(num3)} * {(num4)}= {(answer)}")

            return main()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def maths_solver():

    A = ("addition", "add", "sum")
    D = ("division", "divide")
    S = ("subtraction", "minus", "subtract")
    M = ("multiplication", "multiply")

    user_input = input(
        "Maths Activated What do you want to do (addition,subtaction,etc...) : ")
    user_words = user_input.split()

    for word in user_words:
        if word in A:
            print("Okay you want to add")
            return plus()

        if word in D:
            print("Okay you want to divide")
            return division()

        if word in S:
            print("Okay you want to subtract")
           
            return subtract()

        if word in M:
            print("Okay you want to multiply")
            
            return multiplication()
        else:
            return maths_solver

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == "__main__":
    Data_Write(), welcome(), WishMe(), main()
    Data_Base.write(f" Time of running ({hour}:{minutes})\n")


