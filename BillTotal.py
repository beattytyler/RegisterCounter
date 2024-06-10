# function to call all other functions
def main():
    total = calculateTotal()
    printTotal(total)

# generic functin to handle exceptions
def getNum(prompt = 'Enter Number: '):
    while True:
        num = input(prompt)
        try:
            num = int(num)
            return num
        except:
            print('Invalid number. Please enter a valid number')

# take user input for values
def calculateTotal():
    one = int(getNum('How many one dollar bills do you have?\n'))
    two = int(getNum('How many two dollar bills do you have?\n'))
    five = int(getNum('How many five dollar bills do you have?\n'))
    ten = int(getNum('How many ten dollar bills do you have?\n'))
    twenty = int(getNum('How many twenty dollar bills do you have?\n'))
    fifty = int(getNum('How many fifty dollar bills do you have?\n'))
    oneHundred = int(getNum('How many one-hundred dollar bills do you have?\n'))

# calculate total value with user inputs
    total = 1 * one + 2 * two + 5 * five + 10 * ten + 20 * twenty + 50 * fifty + 100 * oneHundred
    return total

# convert to string and print total
def printTotal(total):
    string_total = str(total)
    print('Your total is: ' + string_total)

# call main
main()