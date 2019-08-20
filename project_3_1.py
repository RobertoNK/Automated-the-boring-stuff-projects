
def collatz(number):
    
    ''' Collatz function - > the simplest imposible math problem '''
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print (3 * number + 1)
        return 3 * number + 1
    
num = input("Enter a number: ")
num = int(num)
while collatz(num) != 1:
    num = int(input ("Re-enter a number : "))
    
