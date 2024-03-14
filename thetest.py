# num = int(input("Enter any number:"))
# newNum = 90
# print(num - (num % 100) + newNum)


def reverseRightMostThreeDigits(number):
    numbers = input().split(',')

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
    mylist = str(numbers).replace(' ', '')
    print(mylist)
    if number in range(0, 1):
        print(number % 10)
    elif number in range(0, 10):
        a = ((number % 10), ((number % 100) // 10), ((number % 1000) // 100))
        print(a)
    elif number in range(10, 100):
        x = ((number % 10), ((number % 100) // 10), ((number % 1000) // 100))
        print(x)
    elif number in range(100, 1000):
        y = ((number // 1000), (number % 10), ((number % 100) // 10), ((number % 1000) // 100))
        print(y)
    elif number in range(1000, 10000000):
        y = ((number // 1000), (number % 10), ((number % 100) // 10), ((number % 1000) // 100))
        print(y)


reverseRightMostThreeDigits(9)
