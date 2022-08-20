a=int(input("enter a numerator"))
b=int(input("enter denominator"))
try:
    answer=a/b
    print(answer)
    print("try completed")
except ZeroDivisionError :
    print("can't divided by zero")

print("program completed")
