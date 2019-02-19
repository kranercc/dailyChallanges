#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.


def transform():
    user = input("Enter Int sperated by \',\': ")
    user = user.split(",")
    user = [int(i) for i in user]
    
    return user

def calc():
    numbers = transform()
    k = int(input("What number you want them added up to be: "))

    n1 = 0
    n2 = 0
    nTotal = 0
    for n in range(len(numbers)):
        if numbers[n] != numbers[-1]: #if there isn't just a last one element in the list
            n1 = numbers[n] #because you can't add up
            n2 = numbers[n+1]
            nTotal = n1+n2

        if nTotal == k:
            print("N1: %d, N2: %d , nTotal: %d , Your Number: %d" % (n1,n2,nTotal,k))
            return True
        
    for n in range(len(numbers)):
        n1 = numbers[n]
        for ni in range(len(numbers)):
            n2 = numbers[ni]
            nTotal = n1+n2
            if nTotal == k:
                print("N1: %d, N2: %d , nTotal: %d , Your Number was hard: %d" % (n1,n2,nTotal,k))
                return True

    return False
        
calc()