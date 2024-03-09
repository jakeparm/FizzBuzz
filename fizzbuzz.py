
#Efficiency is maximized
def fizzbuzz():
    #Loop through numbers 1-100
    for i in range(1, 101):
        #print Fizzbuzz if divisible by both 5 and 3
        if i & 5 == 0 and i & 3 == 0:
            print('FizzBuzz')
        #print Fizz if divisible by 3
        elif i % 3 == 0:
            print('Fizz')
        #print Buzz if divisible by 5
        elif i % 5 == 0:
            print('Buzz')
        #Otherwise print the number
        else:
            print(i)

fizzbuzz()