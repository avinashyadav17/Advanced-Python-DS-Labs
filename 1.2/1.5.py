#exception handling
# try:
#     x=int(input("enter a number:"))
#     result=10/x
#     print(result)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# finally:
#     print("execution completed")

#logging example
import logging
logging.basicConfig(level=logging.INFO)
logging.info("its an info message")
logging.warning("its a warning message")
logging.error("its an error message")
logging.critical("its a critical message")