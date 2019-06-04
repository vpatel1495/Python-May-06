#Assignement 1

#Problem 1
print('Hello My name is "Rishabh". I love Coding')
print('This is my \'first program\'')

x=int(input('What is your first value: '))
y=int(input('What is your second value: '))
z=int(input('What is your third value: '))
print("Value 1 = %d, Value2 = %d, Value 3 = %d" %(x, y, z))

#Problem 2
print( 'Hello! My name is XYX')
print(' \"Hello I am a candidate\"')
print(' \"234.56\" ')
print(' \"34\" ')
print('a + 3j')


#Problem 3
x = 10 + 20 * (45 + 67.0)
#float 2250.0
print(type(x))

x = (True and False) or False
#boolean False
print(type(x))

x = (True or True) and (not False and True)
#boolean True
print(type(x))

x = (3>89) or (34>32)
#boolean True
print(type(x))

x = not True and False
#booleanl False
print(type(x))

#Problem 4
x=int(input('Pick any number: '))
if x%2==0 and x%5==0:
    print('Hurray it is what I am looking for')
else:
    print('wrong input')

#Problem 5

x = int(input('Enter a number: '))
if x>=10 and x<=50:
    print('Yes I am in the range')
else:
    print('Oops')

