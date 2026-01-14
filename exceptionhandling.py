try:
    print(10/0)
except ZeroDivisionError:
    print("cannot divide by zero")



#try-except-else-finally
try:
    x = int(input("enter a number:"))
    y = int(input("enter second number"))
    print(x / y)

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("enter valid input")

else:
    print("division is successful")
finally:
    print("this is finally block")
class invalidageerror(Exception):
    pass
age=int(input("enter your age:"))
if age<18:
    raise invalidageerror("age is not valid")
else:
    print("age is valid")


#try-except-else-finally
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

#raise a TypeError
x=10
if not type(x) is int:
    raise TypeError("only integers are allowed")