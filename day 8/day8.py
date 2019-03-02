'''
This problem was asked by Twitter.

Implement an autocomplete system. 
That is, 

given a query string s 
and a set of all possible query strings,

return all strings in the set that have s as a prefix.

For example, 
given the query string de and the set of strings [dog, deer, deal], return [deer, deal].



basicly show every thing that contains what user has types so far.
looping threw it every time may be too long for a bilion words, maybe implete binary search 
but for the sake of this ex go for loops in a 100 word dictionary


i can use keyboard lib to get REALTIME presses and store all the words until a space is detected
but im going to use the default input function
'''
def wordsAvailable():
    storage = []
    with open("words.txt","r") as words:
        for word in words:
            storage.append(word.strip("\n"))
    return storage

#this is the default method to get it
'''
def userDetection():
    user = input("")
    for word in wordsAvailable():
        if user in word:
            print(word)
userDetection()
'''
wordsAvailable()

def realTimeDetection():
    from keyboard import is_pressed
    from os import system
    from time import sleep
    sleep(1/60) #60 fps to not use too much calculation power

    for word in wordsAvailable(): # for every word in words avaliable
        for l in word: #for every letter in that word
            if is_pressed(l): #if i pressed a letter in that word
                system("cls")
                print(word)
while True:
    realTimeDetection()