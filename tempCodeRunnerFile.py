
def REVERSE(a): 
	a.reverse() 
	return(a) 
def YKNJS(a): 
	b = [] 
	b.extend(REVERSE(a)) 
	print(b) 

a = [1, 3.1, 5.31, 7.531] 


a = [1, 2, 3, 4] 
b = a 
c = a.copy() 
d = a
a[0] = [5] 
print(a, b, c, d) 
fr=["mango","lichi","apple","banana","guava"]
fd=fr
fru=fr.copy()
fruit=fr
fr[0] = ["custardapple"]
fr[-1]=["pomegrante"]
print(fr,fd,fru,fruit)
hindi={
	"name","jyoti"
	"class","b.Tech"
	"love","pyaar"
	"respect","izzat"
	
}
hindi_meaning=input("enter a word")
print(hindi[hindi_meaning])


li = [1, 1.33, 'GFG', 0, 'NO', None, 'G', True] 
val1, val2 = 0,'' 
for x in li: 
	if(type(x) == int or type(x) == float): 
		val1 += x 
	elif(type(x) == str): 
		val2 += x 
	else: 
		break
print(val1, val2) 

a = []
a.append([1, [2, 3], 4])
a.extend([7, 8, 9])
print(a[0][1][1] + a[2])

a = [x for x in (x for x in 'Geeks 22966 for Geeks' if x.isdigit()) if
(x in ([x for x in range(20)]))] 
print(a) 

a = 'Geeks 22536 for 445 Geeks'
b = [x for x in (int(x) for x in a if x.isdigit()) if x%2 == 0] 
print(b) 

a = ['Geeks', 'for', 'Geeks'] 
b = [i[0].swapcase() for i in a] 
print(b) 

li = [2, 3, 9] 
li = [[x for x in[li]] for x in range(3)] 
print (li)

li = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
print (li[1][-1])

a = [10, 20, 30, 40, 50] 
b = [1, 2, 3, 4, 5] 


subtracted = list()
for a, b in zip(a, b):
    item = a -b
    subtracted.append(item)

print(subtracted)

a = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']] 
print(len(a))

li = range(100, 110) 

# statement 2
print (li.index(105))

precision=round(12.8)
print(precision)
print(oct(8))

import keyword
print(keyword.kwlist)
#try-except
try:
	x=3/5
	print(x)
except:
	print("this is an error")


def divide(x, y):
    try:
        # Floor Division : Gives only Fractional Part as Answer
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of Program
divide(3, 2)
def div(p,q):
	try:
		re=p/q
		print(re)
	except:
		print("it may give some error")
div(8,3)

def toy(w,r):
	try:
		return w-r
	except:
		print()
toys=toy(18,5)
print(toys)		
		


# you are given a string prints it's character at even space
n=input("enter a string:")

for i in range(len(n)):
	 if i%2==0:
	
			print(n[i])
i+=1

def find(f):
	fi=""
	for i in range(len(f)):
		if i%2==0:
			fi+=f[i]
	return fi
		
dint=find("jyoti")
print(dint)		
	
# name=input("enter something")
# n1=name[::2]
# print(n1)

x=int(input("enter a number"))
while x>=-2:
    print(x)
	
    x-=2

def jug(y):
	while y>=0:
		print(y)
		y-=1
jug(5)	


r=int(input("enter the number"))
for i in range(r):
	while r<=15:
    		print(r**2)
i+=1

# return "true" if all elements of tuple is different
a=set()
b=tuple(input("enter a tuple list:"))
if len(a)==len(b):
	print("true")
else:
	print("false")
	
a=str(input
("enter a string"))
j=a[::-1]
print(j)

t="jtoyi"
j="".join(reversed(t))
print(j)
def welcomeAboard(name):
    return "welcome jyoti"
print(welcomeAboard("joti"))    

def trim(str):
    
    return str
print(trim(str.lower("JYOTILOVEYOUALOT")))
print(trim(str.upper("when willyou")))
print(trim(str.title("kYu yaar")))
print(trim(str.swapcase("kya Batau")))


i=(1,7,4,"you")
print(i.index("you"))

you=input("enter something")
if you.endswith("g"):
    print("yes")
else:
    print("no")
def gfg(S):
    b = S.lower()
    if ('''Your code here'''):
        print("Yes")
    else:
        print("No")
while True:
    you=input("enter kuch bhi...")
   
    if you.endswith("A"and "Z"):
        print("yes🎇🎆")
    break
   
else:
    print("no❌📛")
        
while True:
    you = input("enter kuch bhi...")
    if you.endswith(("A", "Z")):
        print("yes🎇🎆")
        break
    else:
        print("no❌📛")

you = input("enter kuch bhi...")
if you.endswith(("A", "Z")):
    print("yes🎇🎆")
else:
    print("no❌📛")


# i want to make a breakfast payment details of a restaurant
menu={
    "paratha":"25",
    "bhujiya":"30",
    "lassi":"15",

}
print("you are welcomed to our resturant 😊")
print("Our Menu is\n Paratha :25rs \n bhujiya :30rs \n lassi: 15rs")
#to add all the menu bill
order_pay=0
item=input("Please enter your first dish:")
if item in menu:
    #to add
    order_pay += menu[item]
    print(f"your dish {item} is confirmed✅")
else:
    print(f"Sorry😓this {item} is not avaialable now")
item2=input("enter your second order if you are desired to eat this..🌟 (yes/no)")
if item2=="yes":
    if item2 in menu:
        print("your second order is also confirmed✅")
        order_pay+=menu[item2]
    else:
        print("sorry again")

print(f"your bill is {order_pay}") 

# add the matrix of any order
def matrix(p,q):
    re=[]
    for i in range(p):
        rs=[]
        for j in range(q):
            ip=int(input(f"enter the values of i and j that is {i} and {j}"))
            rs.append(ip)
        re.append(rs)   
    return re 
def ab(A,B):
    result=[]
    for i in range(len(A)):
        rs=[]
        for j in range(len(A[0])):
            rs.append(A[i][j]+B[i][j])
        result.append(rs)
    return result    
p=int(input("enter the value of p \n:"))
q=int(input("enter the value of q \n :"))
A=matrix(p,q)
print(f"the given matrix is {A}")   
B=matrix(p,q)
print(f"the given matrix is{B}") 

D=ab(A,B)
print(f"sum of the given matrix is{D}")

l=["jyoti","you","chittu","nayan","jayan","Jitu"]
for i in l:
    if i.startswith("j"):
        print(f"hello {i}")

n=int(input("enter a table for multiplication")) 
i=10
while i>=1:
    print(f"{n}*{i}={n*i}") 
    i-=1      

m=int(input("enter a number:"))
i=2
for i in range(2,m-1):
    if m%i==0:
        print(" not prime")
        break
else:
    print("prime")

def prime(j):
    for i in range(2,j-1):
        if j%i==0:
            return "NOT PRIME"
        return "PRIME "
    
pe=prime(72)
pr=prime(7)
print(pr)
print(pe)
num=int(input("enter a number:"))
fact=1
for u in range(1,num+1):
    fact*=u
print(fact)

num1=int(input("enter a  number:"))
i=1
su=1
while i<=num1:
    su*=i
    i+=1
print(su)

row=int(input("enter a row for printing this star:"))
for i in range(1,row+1):#make rows value of i=1,2,3,4,5 when row=5
    print(" "*(row-i),end=" ")#gives spaces yha hume us given number me se i ki value of minus karna hai agar hum humesha 1 ko row me minus karenge to same hi space print hoga
    print("*"*i,end=" ")#prints star for simple jitna bhi baar i ka value hoga utna star print hoga
    print()#gives a new line
row1=int(input("enter a number for row"))    
for u in range(1,row+1):   
    print(" "*(row1-i),end=" " )
    print("*"*(2*i-1),end=" ")
    print()

row2=int(input("enter the row:"))
for i in range(1,row2+1):
    print(" "*(row2-i),end=" ")
    print("*"*(2*i-1))


#print stars in pyramid shape
row=int(input("enter the row"))
for i in range(1,row+1):
    print(" "*(row-i),end=" ")#gives space
    print("*"*(2*i-1))#it prints the stars

row1=int(input("enter the  row:"))#5
for j in range(1,row+1):#1,2,3,4,5
    print(" "*(row1-j))#5-1=4 gives four spaces then it comes to the next line it prints 
    print("*"*j,end=" ")
#print inverted star
row2=int(input("enter the row for inverted star::"))#5
for k in range(row2,0,-1):#54321
    print(" "*(row2-k),end=" ")
    print("*"*(2*k))

#how many days i'll alive
age=int(input("enter your age:"))
print(f"the days you will alive i.e{age*365}")    

a=34 
b=80
print( not a>=b , not a<=b)
print(min(a,b))
print(max(a,b))
j="youAreMine"
print(j[1:10:2])
print(j[::-4])
print("love".zfill(-1))
print(j.casefold())
print(j.center(7))
print(j.encode())

letter='''Dear |name|,
        now you are mine❣️
        
            because |no|'''
print(letter.replace("|name|","Jyoti").replace("|no|","i love you so much✨"))
print(letter.splitlines().sort())

fruit=["mango","apple","banana","lichi","grapes","custard apple"]
fruit1=input("enter first favourite fruit:-")
fruit2=input("enter the second favourite fruit:-")
fruit3=input("enter your third favourite fruit:-")
if fruit1 in fruit:
    print(f"{fruit1} these fruits are my favourite 😘")
elif fruit2 in fruit:
    print(f"{fruit2} is also my favourite")
else:
    print(f"{fruit3} this is tantative")

studentsMarks=[]
marks1=int(input("enter the marks of a student:-"))
studentsMarks.append(marks1)
marks2=int(input("enter the marks of 2nd student:-"))
studentsMarks.append(marks2)
marks3=int(input("enter the marks of 3rd student:-"))
studentsMarks.append(marks3)
marks4=int(input("enter the marks of 4th student:-"))
studentsMarks.append(marks4)
marks5=int(input("enter the marks of 5th student:-"))
studentsMarks.append(marks5)
if marks1 in studentsMarks:
    print(studentsMarks)
studentsMarks.sort()
print(studentsMarks)

word={
    "kitab":"book",
    "rabad":"eraser",
    "katar":"sharpner",
    "thand":"cold",
    "garm":"hot",
    "kamjor":"weak"

}
your_word=input("enter your wordmeaning:\n")
if your_word in word:
    print(f" the meaning of this word is: \n {word[your_word]} 😊")
else:
    print( word[your_word])


eightnumbers=set()
st1 = int(input("enter your marks:-"))
eightnumbers.add(st1)

st2 =int(input("enter your marks:-"))
eightnumbers.add(st2)

st3 =int(input("enter your marks:-"))
eightnumbers.add(st3)

st4 = int(input("enter your marks:-"))
eightnumbers.add(st4)

st5 = int(input("enter your marks:-"))
eightnumbers.add(st5)

st6 =  int(input("enter your marks:-"))
eightnumbers.add(st6)

st7 = int(input("enter your marks:-"))
eightnumbers.add(st7)

st8 = int(input("enter your marks:-"))
eightnumbers.add(st8)
for i in eightnumbers:
    if i%2==0:
        print(i)
    else:
        print()

frnd_Dict={}
name=input("enter your name :")
language=input("please  give your desired language:")
frnd_Dict.update({name:language})
name1=input("give your name:")
language1=input("enter your favourite language:")
frnd_Dict.update({name1:language1})
name2=input("enter your name:")
language2=input('give your language:')
frnd_Dict.update({name2:language2})
# print(frnd_Dict)


sum=0
print("Please Welcome to Our grocery shop✨")
user_product=input("what do you want to purchase:")
user=int(input("Tell me the price of this :"))
        
if user!="q":
            
    print(f"you bill of this {user_product} is about {user}")
    print("if you wanna to buy something else, please tell us!")
    user1=(input("do you want to buy (yes/no)"))
        
if user1=="yes":
                
    print("tell us ,what?")
    user_pro1=input("show me ")
    user2=int(input("the price is"))
    print(f"the price of  {user_pro1} is {user2} ")
            
    sum+=user2+user
    print(f"your total bill this {sum}")
 
else:
    sum+=user
    print("please come!")
    print(f"your total bill is {sum}")
        
    

    