'''Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
 count the number of ways it can be decoded.

For example, the message '111' would give 3,
 since it could be decoded as 'aaa', 'ka', and 'ak'.'''


lettersAndValues = {

}

for i in range(97,123):
    lettersAndValues[chr(i)] = str(i- 96 )


def numbersToLetters(): #error on keys idk why, im looking for a way to solve it
    pass



def lettersToNumbers(): #encode your message to numbers
    global lettersAndValues
    user = input("Type numbers to decode the message: ")
    for n in user:
        if n in lettersAndValues.keys():
            print(lettersAndValues[n],end='')

lettersToNumbers()