my_name=input('enter yor name')
my_age=int(input('enter your eage'))
print(f'my name is{my_name}and i am{my_age}years old')
first_number=int(input('enter first number'))
second_number=int(input('enter second number'))
operation=input('what is the operation(+-*/)')
if operation== '+':
    print(first_number + second_number)
elif operation== '-':
    print(first_number - second_number)
elif operation== '/':
    print(first_number / second_number)
elif operation== '*':
    print(first_number * second_number)

else :
    print('the operation is not vaild')

bus_capacity=50
people_inbus=int(input('how many people are in the bus?'))
people_outbus=int(input('how many people are want to enter the bus?'))
empty_seats=bus_capacity -people_inbus 




if empty_seats > people_outbus :
    print('the empty seats is{empty_seats}')
elif empty_seats <= people_outbus :
    print('the bus is full')

