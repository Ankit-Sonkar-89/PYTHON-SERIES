print(" strings and numeric value can operate together with * ")

a , b = 2, 3 
txt = "@"
print(2*txt*3)

print(" string and string can operate with + ")

a , b = "2" , 3
txt = "@"
print((a+txt)*b)

print(" numeric values can operate with all arthimetic operators ")

a , b = 2, 3 
c = 4
print( a+b*c)

print(" arthimetic expression with integer float will result in float ")
a , b = 10 , 5.0
c = a * b 
print(c)

print(" result of divison operator with two integers will be float ")

a , b = 1 , 2
c = a/b
print(c)

print(" integer divison with float and int will give int displayed as float ")

a , b = 1.5 , 3
c = a//b
print(c , a/b )

print(" floor gives closest integer , which is lesser than or equal to the float value . - result of (a//b) is same as floor (a/b )")

a , b = 12 , 5
c = a//b
print(c)

a , b = -12 , 5 
c = a // b 
print(c)

a , b = -12 , -5
c = a // b 
print(c)

print(" remainder is negative when determinant is negative ")

a , b = -5 , 2 
c = a%b
print(c)

a , b = 5 , 2
c = a%b
print(c)

a , b = 5 , -2
c = a%b
print(c)
