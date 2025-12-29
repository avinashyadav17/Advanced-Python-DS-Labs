#functions and lambda
def add(a,b=5):
    return a+b
print(add(10))

square=lambda x:x*x
print(square(4))

numbers=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda x:x%2==0,numbers))
print(even)