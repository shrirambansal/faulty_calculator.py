# 45 * 3 = 555
# 56 + 9 = 77
# 56 / 6 = 4
import pstats


print("\t***Welcome in faulti calculator***\t")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("\t***Please choose an one operator***\t")
print("for sum ('+') enter 0 .")
print("for substract ('-') enter 1 .")
print("for multipli ('*') enter 2 .")
print("for divide ('/') enter 3 .")
choose = int(input("Enter the choose : "))

if choose == 0 :
    sum = num1 + num2
    if (num1 ==56 and num2 ==9) or (num1 ==9 and num2 ==56) :
        print(f"Sum of {num1} and {num2} is 77")
        pass
    else :
        print(f"Sum of {num1} and {num2} is {sum}")
        pass
    pass

elif choose == 1 :
    sub = num1 - num2
    print(f"Subract of {num1} and {num2} is {sub}")
    pass

elif choose == 2 :
    multi = num1 * num2
    if (num1 ==45 and num2 ==3) or (num1 ==3 and num2 ==45) :
        print(f"multiply of {num1} and {num2} is 555")
        pass
    else :
        print(f"multilpy of {num1} and {num2} is {multi}")
        pass
    pass

elif choose == 3 :
    divide = num1 / num2
    if (num1 ==56 and num2 ==6) or (num1 ==6 and num2 ==56) :
        print(f"divide of {num1} and {num2} is 4")
        pass
    else :
        print(f"divide of {num1} and {num2} is {divide}")
        pass
    pass

else :
    print("you enter invalid key word")

