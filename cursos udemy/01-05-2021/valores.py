# import math

# a = 2
# b = 3
# h = math.sqrt(a**2+b**2)
# print(h)

# a = 8+2*3/4-2**3
# b = 4*(3+5*5-2)
# c = 3>4<5 and 3<2 or 2!=4 and 4==2+2 or not True

# a =10
# b =12
# c=5

# print(b*c==6*a)




# x =1

# if x%2 ==0:
# #     print('el numero es par')
# # else:
# #     print('el numero es inpar')

# x = 1+4*3+8/2*4+5**2

# if x % 2 ==0:
#     x+=1
# else:
#     x+=2
# print(x)

# Fibonacci


# def fib(n):    
#     a = 0
#     b = 1

#     for k in range(n):
#         c = a+b
#         a = b
#         b = c

#     return b

# for x in range(35):
#     print(fib(x))


# fib(35)

# Rango

# list(range(2,13,2))
# for list in range(2,13,2):
#     print(list)


s = 0

for n in range(1, 10):

     if n % 7 == 0:

         break;

     s += n

print(s)


s = 0

for n in range(1, 10):

     if n % 2 == 0:

         continue;

     s += n
    
print(s)



s = 0

for n in range(1, 10):

     if n % 11 == 0:

         break;

     s += n

else:

     s += 10

print(s)


s = 0

for n in range(1, 10):

     if n % 2 == 0:

         pass;

     s += n

print(s)



s = 0

for n in range(1, 10):

     if n % 2 != 0:

       continue;

     s += n

else:

      s += 5

print(s)