'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
'''
example1 = [3,4,-1,1]
example2 = [1,2,0]

def findLowest(listOfElements):
    highest = max(listOfElements) #biggest element in the list
    lowest = min(listOfElements) #lowest in the list
    isThereAnyErr = False #if there is an error such like the list is incomplete, don't give me the next highest value like [1,2,0] > 3
    for n in range(lowest,highest): #the numbers from -1 to 4 ( first example )
        if n+1 in listOfElements: #if the next number is in the list check it like ( -1 > 0 , 1 > 2 ERR , 3 > 4)
            print("by now the list is ok: ",n+1)
        else:
            if n+1 == 0: #ignore zeroes like i saw in the example, in the first should've gave 0 cuz -1 then 1 is missing 0 so i added a rule
                continue
            print("missing element is: ",n+1)
            isThereAnyErr = True
    if isThereAnyErr == False: #here it gives you the next highest value in the list if the list dosnt have any errors such like being incomplete
        print("Next highest element is: ",highest+1)
    else:
        print("the list is incomplete")



findLowest(example1)