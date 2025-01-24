loop=1
numbers =[]
while loop!=6:
    try: 
        num=int(input('Hi please enter a number: '))
        numbers.append(num)
        print(loop)
        loop=loop+1

    except ValueError:
        print('This is an invalid input')

answer=max(numbers)-min(numbers)
print('Difference between MAX AND MIN: ',answer)
