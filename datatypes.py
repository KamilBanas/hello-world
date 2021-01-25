import math

#Demo of strings
mypet = "dog"
yourpet = 'cat'
print("My pet is a " + mypet)
arePetsEqual = mypet == yourpet
print("Do we have the same animals? " + str(arePetsEqual))

print("Do we have the same animals? " + str(mypet == yourpet))

print(type(arePetsEqual))
print(type(mypet))

myNumber = 123
myFloatNumber = 12.34
print(type(myNumber))
print(type(myFloatNumber))

complexNumber = 5j

whatType = myNumber / myFloatNumber
print("what type?", whatType)

#anError = int(mypet)

print(int("987"))

total = 0
total = total + 10
print("total =", total)

#short way for total = total + 10 :
total += 10
total *= 10
print("total =", total)

remainder = total % myNumber
print("Remainder =", remainder)

print(math.pi)
math.pow(5, 10)
print(math.pow(5, 10))

#precedence
first = 1
second = 2
third = 3
print(first + second * third)
print((first + second) * third)

data = "Hi there"
for index in range(len(data)):
    print(index, data[index])







