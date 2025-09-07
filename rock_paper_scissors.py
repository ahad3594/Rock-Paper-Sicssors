import random

computer= random.choice([1,2,3])

name = input('Enter your name: ')

you=input('''Choose:
             Rock    :    R
             Paper   :    P
             Scissor :    S  
                 
                  ''')

you_ch={"R" : 1, "P" : 2,"S" : 3}
book={1: "Rock" , 2 : "Paper", 3 :"Scissor"}

choose=you_ch[you]

print(f'YOU CHOOSED: {book[choose]}\nCOMPUTER CHOOSED: {book[computer]}')

if(choose==computer):
    print("DRAW")

else:
    if(choose==1 and computer==2):

        print("COMPUTER WINS 👑")
     
    elif(choose==1 and computer==3):

        print(f"{name} WINS 😎")

    elif(choose==2 and computer==1):

        print(f"{name} WINS 😎")

    elif(choose==2 and computer==3):
    
        print("COMPUTER WINS 👑")

    elif(choose==3 and computer==1):

        print("COMPUTER WINS 👑")

    else:

        print(f"{name} WINS 😎")


