myvariable = "mathew"
print(myvariable)

x = 10 
x = "hello"
print(x)

a, b, c = 1, 2, 3 
print(a)
print(b)
print(c)


# scape sequences 
# \b = back space 

# escape new line +\
print("hello \
world \
python")

print("123456\rabcd")

mstringthree = "this is single code 'hay'"
print(mstringthree)

#z.fill
c, d, e = "1" ,"11","111"
print(c.zfill(3))
print(d.zfill(3))
print(e.zfill(3))

#center()
a = "miso"
print(a.center(8, "#"))

#count()
b = "i python love python"
print(b.count("python"))

c = "hello one two one two"
print(c.replace("one", "1"))

# old formatting 
name = "mathew"
age = 21
rank = 10
print("my name is: " + name)
#print("my name is: "+ "name and my age" + age) #error
print("my name is %s" % "mathew")
print("my name is %s and my age is %d" % (name, age))
print("my name is %s and my age is %d and my rank is %.1f" % (name, age, rank))
# %s = string
# %d = number
# %(no. of zeros)f = float

#new formatting

name = "mathew"
age = 21
rank = 10
print("my name is " + name)
#print("my name is: "+ "name and my age" + age) #error
print("my name is {}" .format ("mathew"))
print("my name is {} and my age is {}" .format (name, age))
print("my name is {:s} and my age is {:d} and my rank is {:d}" .format (name, age, rank))

#{:s} = string
# {:d} = number
# {:f} = float

# format money

mymoney = 500160350199

print("my money in bank is {:d}".format(mymoney))
print("my money in bank is {:,d}".format(mymoney))
print("my money in bank is {:_d}".format(mymoney))

#rearrange items

a, b, c = "one", "two", "three"
print("hello {} {} {}".format(a, b, c)) 
print("hello {1} {2} {0}".format(a, b, c)) 

# format in version 3.6+

myname = "mathew"
myage = 21 

print(f"my name is {myname} and my age is {myage}")
# (f)

#numbers
#add

print(10 + 30)
print(-10 + 20)

#subtract

print(30 - 10)

#multiple
print(10 * 3)
print(5 + 10 * 100)
 
 #divide

print(100 / 20)
print(int(100 / 20))

#modulus 
print(8 % 2) #0
print(9 % 2) #1
print(20 % 5) #0
print(22 % 5) # 2

# exponant

print(2 ** 5)
print(2 * 2 * 2 * 2 * 2)
print(5 ** 4)
print(5 * 5 * 5 * 5)
 

 #floor division

print(100 // 20) #5
print(119 // 20) #5
print(120 // 20) #6
print(139 // 20) #6
