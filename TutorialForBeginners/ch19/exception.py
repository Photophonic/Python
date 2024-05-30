# Custom exception
class MyCustomException(Exception):
    pass


x = 2
# use try/except blocks to evaluate and catch errors
try:
    raise MyCustomException("My exception")
    # print(x / 1)
    if not type(x) is str:
        # manually raising an error
        raise TypeError("Only strings please.")

except NameError:
    print("NameError - undefined variable")
except ZeroDivisionError:
    print("Zero divide")
except Exception as error:
    # behives like when others error in PL/SQL
    print(error)
# use the else to continue on if there are no errors
else:
    print("No errors")
# finally blocks will be run regarldess of error or not
finally:
    print("This is the finally block")
