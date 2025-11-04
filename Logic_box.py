print('Welcome To Pattern Generator And Number Analyzer Programme !!')
print()
print()
print('Select Your Choice From Below :- ')
print('-----------------------------------------------------------------------')
print()
print('1. Right Angled Triangle .')
print('2. Pyramid .')
print('3. Left Angled Triangle .')
print('4. Analyze A Range Of Numbers .')
print('Instruction :- Please Enter The Valid Choice For Better Experience...!!')
print()
print('-----------------------------------------------------------------------')

choice = int(input('Enter Your Choice :- '))

if (choice == 1) or (choice == 2) or (choice == 3):
    rows = int(input('Enter The Number Of Rows For The Pattern :- '))

print()


if (choice == 1) or (choice == 2) or (choice == 3):
    print('Here Is Your Pattern :- ')
else:
    print('Here Is The Analysis Of Your Given Range Of Numbers :- ')


print()
print()


if choice == 1:
    print('Right Angled Triangle...!!')
    print()
    for i in range(1,rows+1):
        for j in range (rows,i-1,-1):
            print(' ',end='')
        for k in range(1,rows-i+1):
            print('*',end='')
        print()

elif choice == 2:
    print('Pyramid...!!')
    print()
    for i in range(1,rows+1):
        for j in range (1,rows-i+1):
            print(' ',end='')
        for k in range(1,i+1):
            print('*',end=' ')
        print()

elif choice == 3:
    print('Left Angled Triangle...!!')
    print()
    for i in range(1,rows+1):
        for k in range(1,i+1):
            print('*',end='')
        print()

elif choice == 4:
    srange = int(input('Enter The Start Of The Range :- '))
    erange = int(input('Enter The End Of The Range :- '))
    sum = 0
    for i in range (srange,erange+1):
        sum = sum + i
        if i % 2 == 0:
            print('Number ',end='')
            print(i,end='')
            print(' Is Even.')
        else:
            print('Number ',end='')
            print(i,end='')
            print(' Is Odd.')
    print()
    print('The sum of all numbers from ',end='')
    print(srange,end='')
    print(' to ',end='')
    print(erange,end='')
    print(' is = ',sum)    
else:
    print('Please Enter The Valid Choice .... !!')


print('Thank You...!!')
