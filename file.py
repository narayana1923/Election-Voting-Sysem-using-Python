from random import*
from matplotlib.pyplot import*
from pandas import*
from datetime import*
from time import*
def tried():
    try:
        num=int(input("Enter number of students: "))
        if num<=62:
            while num<1:
                print("The number of students should be greater than 0")
                sleep(1)
                num=int(input("Re-enter number of students: "))
        else:
            while num>62:
                print("The total number of students in csseb is 62\nso, number of students should be less the 63")
                num=int(input("Re-enter number of students"))
    except ValueError:
        while True:
            try:
                num=int(input("Please Re-enter number of students only in integer: "))
                while num<1:
                    print("The number of students should be greater than 0")
                    sleep(1)
                    num=int(input("Re-enter number of students: "))
                else:
                    while num>62:
                        print("The total number of students in csseb is 62\nso, number of students should be less the 63")
                        num=int(input("Re-enter number of students"))
                    else: break
            except ValueError:
                print("Number of students must be an integer")
    student(num)
def student(n):
    global df
    candidate1,candidate2,candidate3='X','Y','Z'
    d={}
    list,list1,list2=[],[],[]
    print('to vote candidate1 enter x as your vote')
    sleep(0.5)
    print('To vote candidate2 enter y as your vote')
    sleep(0.5)
    print('To vote candidate 3 enter z as your vote')
    sleep(1.5)
    for i in range(n):
        if i%10==0 and i!=0:
            print('to vote candidate1 enter x as your vote')
            print('To vote candidate2 enter y as your vote')
            print('To vote candidate3 enter z as your vote')
            sleep(1)
        s=input('Enter atleast last two characters of your Roll number: ').upper()
        s=roll(s)
        if s not in d:
            v=input("Enter your vote: ").upper()
            if candidate1==v: list.append(v)
            elif candidate2==v: list1.append(v)
            elif candidate3==v: list2.append(v)
            else:
                v=check_vote(v,candidate1,candidate2,candidate3)
                if candidate1==v: list.append(v)
                elif candidate2==v: list1.append(v)
                else: list2.append(v)
            d.update({s:v})
        elif s in d:
            while s in d:
                print("The roll number you entered is already entered")
                sleep(1)
                s=input("Please enter atleast last two characters of your Roll number: ").upper()
                s=roll(s)
            else:
                v=input("Enter your vote: ").upper()
                if candidate1==v: list.append(v)
                elif candidate2==v: list1.append(v)
                elif candidate3==v: list2.append(v)
                else:
                    v=check_vote(v,candidate1,candidate2,candidate3)
                    if candidate1==v: list.append(v)
                    elif candidate2==v: list1.append(v)
                    elif candidate3==v: list2.append(v)
            d.update({s:v})
    n,n1,n2,n3=len(list),len(list1),len(list2),len(d)
    d.clear()
    winner(n,n1,n2)
    pied(n,n1,n2,n3)
def roll(s):
    global df
    while True:
        if len(s)<10 and len(s)>1:
            if len(s)==2:
                for i in df['rollnumber']:
                    if s in i[8:10]: return i
                else:
                    print("your roll number not found in our data base")
                    sleep(1)
                    s=input("Re-enter your full roll number: ").upper()
            else:
                for i in df['rollnumber']:
                    if s in i: return i
                else:
                    print("your roll number not found in our data base")
                    sleep(1)
                    s=input("Re-enter your full roll number: ").upper()
        elif len(s)==10:
            for i in df['rollnumber']:
                if s==i: return i
            else:
                print("your roll number doesn't belong to csseb")
                sleep(1)
                s=input("enter a valid roll number: ").upper()
        else:
            print("your roll number is invalid")
            sleep(1)
            s=input("re enter your roll number: ").upper()
def check_vote(v,candidate1,candidate2,candidate3):
    while v!=candidate1 and v!=candidate2 and v!=candidate3:
        print('enter an valid vote,valid votes are x,y,z')
        sleep(1)
        v=input('Enter your vote again: ').upper()
    else: return v
def check_ask(ask):
    while ask!='YES' and ask!='NO': ask=input("Enter only yes or no: ").upper()
    else: return ask
def winner(n,n1,n2):
    if n>n2 and n>n1:
        print("CANDIDATE 1 IS WINNER WITH {} VOTES".format(n))
        sleep(1)
    elif n1>n2 and n1>n:
        print("CANDIDATE 1 IS WINNER WITH {} VOTES".format(n1))
        sleep(1)
    elif n2>n and n2>n1:
        print("CANDIDATE 1 IS WINNER WITH {} VOTES".format(n2))
        sleep(1)
    elif n==n1 and n>n2:
        print("Candidate 1 and candidate 2 got same and highest votes that is {} votes".format(n))
        sleep(1)
        ask=input("Enter yes if you want to pick a random winner among the two? ").upper()
        ask=check_ask(ask)
        if ask=='YES': print("\n\t\t\t{} IS THE WINNER\n\n".format(choice('XY')))
        else: print("Ok, do an alternative or reconduct the elections")
    elif n==n2 and n>n1:
        print("Candidate 1 and candidate 3 got same and highest votes that is {} votes".format(n))
        sleep(1)
        ask=input("Enter yes if you want to pick a random winner among the two? ").upper()
        ask=check_ask(ask)
        if ask=='YES': print("\n\t\t\t{} IS THE WINNER\n\n".format(choice('XZ')))
        else: print("Ok, do an alternative or reconduct the elections")
    elif n1==n2 and n1>n:
        print("candidate 2 and candidate 3 got same and highest votes that is {} votes".format(n1))
        sleep(1)
        ask=input("Enter yes if you want to pick a random winner among the two,else no: ").upper()
        ask=check_ask(ask)
        if ask=='YES': print("\n\t\t\t{} IS THE WINNER\n\n".format(choice('YZ')))
        else: print("Ok, do an alternative or reconduct the elections")
    else:
        print("All the candiadates got same votes that is {} votes".format(n))
        sleep(1)
        ask=input("Enter yes if you want to pick a random winner among the three,else no: ").upper()
        ask=check_ask(ask)
        if ask=='YES': print("\n\t\t\t{} IS THE WINNER\n\n".format(choice('XYZ')))
        else: print("Ok, do an alternative or reconduct the elections")
def pied(n,n1,n2,n3):
    per=[(n/n3)*100,(n1/n3)*100,(n2/n3)*100]
    hmm=['candidate1','candidate2','candidate3']
    cols=['blue','white','green']
    if n>n1 and n>n2: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0.2,0,0),shadow=True,autopct='%.1f%%')
    elif n1>n and n1>n2: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0,0.2,0),shadow=True,autopct='%.1f%%')
    elif n2>n1 and n2>n: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0,0,0.2),shadow=True,autopct='%.1f%%')
    elif n==n1>n2: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0.2,0.2,0),shadow=True,autopct='%.1f%%')
    elif n==n2>n1: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0.2,0,0.2),shadow=True,autopct='%.1f%%')
    elif n2==n1>n: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0,0.2,0.2),shadow=True,autopct='%.1f%%')
    else: pie(per,labels=hmm,colors=cols,startangle=90,explode=(0,0,0),shadow=True,autopct='%.1f%%')
    title('Percentage of votes')
    show()
try:
    # You need a file with roll numbers/ids of the voters
    df=read_csv("empdata.csv")
    t=datetime.now()
    print("\t0_0 WELCOME TO NASAYA VOTING SYSTEM 0_0\t",date.today(),t.strftime("%I:%M:%S %p"))
    sleep(1)
    tried()
    print("\t\tCandidates Who Lost Please Don't be disappointed",sleep(1),"\n\n\t  You may not win immediately but you will win definitely ;-)")
    sleep(1)
    print("\n\t\t_/\_ THANK YOU FOR USING NASAYA VOTING SYSTEM _/\_\t\t\n\n","\t"*9,date.today(),t.strftime("%I:%M:%S %p"))
except FileNotFoundError:
    print("Enter the correct location of empdata.csv and re run the program")