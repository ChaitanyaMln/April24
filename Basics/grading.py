maths=int(input("Enter the marks maths :"))
science=int(input("Enter the marks science :"))
social=int(input("Enter the marks social :"))
average=(maths+science+social)//3

if(average>=90 and average<=100):
    print("A1")
elif(average>=80 and average<90):
    print("A2") 
elif(average>=70 and average<80):
    print("B1")
elif(average>=60 and average<70):
    print("B2") 
elif(average>=35 and average<60):
    print("C1")             
elif average>=34 :
    print("F")    
