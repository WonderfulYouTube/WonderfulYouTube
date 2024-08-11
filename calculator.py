

def divisionTime() :
    xd = "Enter your first number"
    print(xd)
    xdi = int(input())
    yd = "Enter second number"
    print(yd)
    ydi = int(input())
    print("Your answer is")
    print(xdi/ydi)
    tryAgain()
    
def multiplicationTime() :
    xm = "Enter your first number"
    print(xm)
    xmi = int(input())
    ym = "Enter second number"
    print(ym)
    ydi = int(input())
    print("Your answer is")
    print(xmi*ydi)
    tryAgain()
    
def additionTime() :
    xa = "Enter your first number"
    print(xa)
    xai = int(input())
    ya = "Enter second number"
    print(ya)
    ydi = int(input())
    print("Your answer is")
    print(xai+ydi)
    tryAgain()

def subtractionTime() :
    xs = "Enter your first number"
    print(xs)
    xsi = int(input())
    ys = "Enter second number"
    print(ys)
    ysi = int(input())
    print("Your answer is")
    print(xsi-ysi)
    tryAgain()
    
def tryAgain() :
    tryagainprompt = "Would you like to try again?"
    print(tryagainprompt)
    tryagainprompti = input()
    if tryagainprompti == "yes" :
        tryAgainphasetwo()
    else :
        print("Thank you for using calculator")

def tryAgainphasetwo() :
    askprompt = "What operation would you like to do? Addition/Subtraction/Division/Multiplication? Please do not put capital letters in your answer."
    print(askprompt)
    askprompti = input()
    if askprompti == "addition" :
        additionTime()
    if askprompti == "subtraction" :
        subtractionTime()
    if askprompti == "division" :
        divisionTime()
    if askprompti == "multiplication" :
        multiplicationTime()
 

tryAgainphasetwo()
    
def tryAgain() :
    tryagainprompt = "Would you like to try again?"
    print(tryagainprompt)
    tryagainprompti = input()
    if tryagainprompti == "yes" :
        tryAgaintwo()
    else :
        print("Thank you for using calculator")
    
    

