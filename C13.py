person = {'first_name':'Vladut','last_name':'Lorincz','birth_year':1999,'children':['Nathalie','Ethan']}

for i in person:
    print(i,":",person[i])

dictionary={'Numbers':[1,2,3,4,5],'Letters':['A','B','C','D']}

for elements in dictionary:
    print("These are ",elements)
    for under in dictionary[elements]:
        print(under)

print("-------------------------")
print("Data Validation")
print("-------------------------")

oknumber = False

while oknumber == False:
    no = int(input("Input a number between 1 and 10:"))
    if(no<1 or no >10):
        print("Wrong number! Enter again")
        continue
    else:
        oknumber = True
print(no)

print("-------------------------")
print("Data Validation With Error Handling")
print("-------------------------")

enteredno = input("Enter a number between 100 and 200: ")
try:
    breakout = False
    enteredno = int(enteredno)
    while breakout==False:
        if(enteredno>=100 and enteredno<=200):
            print("Works fine! The number is: ",enteredno)
            breakout = True
        else:
            print("Enter a number between 100 and 200!")
            continue
except:
    print("You entered a wrong number or string")