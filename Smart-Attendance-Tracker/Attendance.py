n=int(input("Enter the Number of students: "))
Student=[]
Reg=[]
SubNum=[]
Subject=[]
Total=[]
Present=[]
t=0
for i in range(n):
    Student.append(input(f"Enter the Name of Student {i+1}: "))
    Reg.append(input(f"Enter the Registration Number of Student {i+1}: "))
    x=int(input("Enter the Number of Subjects: "))
    SubNum.append(x)
    for j in range(t,x+t):
        Subject.append(input(f"Enter the Name of the Subject {j+1}: "))
        p=int(input(f"Enter the Total Number of Working Days in {Subject[j]}: "))
        Total.append(p)
        while True:
            q=int(input(f"Enter the Number of Days, Student {i+1} is Present in {Subject[j]}: "))
            if(q<=p and q>-1):
                Present.append(q)
                break
    t=t+x
              
def display(j):
    m=(Present[j]/Total[j])*100
    if m>=90:
        status="Excellent-Keep Going"
    elif m>=80:
        status="Good-Try to Improve"
    elif m>=75:
        status="Satisfactory-Improvement Needed"
    else:
        status="Critical-Attend Classes strictly"
    print(Subject[j],":",m,"  ",status)

print("\n\n")
print("========Attendance Report========")
a=0
c=0
while True:
    print("1.To View Attendance Report Of all Students \n2.To View Attendance Report of One Specific Student\n3.Exit")
    a=int(input("Enter a Choice: "))
    if(a==1):
        t=0
        for i in range(n):
            print("Name: ",Student[i])
            print("Registration No.: ",Reg[i])
            for j in range(t,(SubNum[i]+t)):
                display(j)
            t=t+SubNum[i]
            print("\n")
    elif(a==2):
        t=0
        cc=0
        f=input("Enter a Student Registration Number: ")
        for i in range(n):
            if(f==Reg[i]):
                c=i
                break
            elif (i==n-1):
                cc=1
                print("Registration Number Not Found...")

        if(cc!=1):
            for i in range(c):
                t=t+SubNum[i]
            print("Name: ",Student[c])
            print("Registration No.: ",Reg[c])
            for j in range(t,SubNum[c]+t):
                display(j)
            print("\n")
    elif(a==3):
        break
    else:
        print("Enter a valid Choice...\n\n")