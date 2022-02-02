###### implementation of pascal's triangle in python

def pascal(num1: int,num2: int)->int:
    if (num1 == num2) or (num2 == 0):
        return 1
    elif (num2 > num1):
        return 0
    else:
        return pascal(num1 -1, num2-1) + pascal(num1-1, num2)

if __name__ == '__main__':
    num1, num2 = int(input()), int(input())
    result = pascal(num1, num2)
    print(result)
