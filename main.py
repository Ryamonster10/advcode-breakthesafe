from random import randint 

def randomWord():
    r = randint(1,26)
    a = chr(r+26)
    return a

random = [randomWord(),randomWord(),randomWord()]





def guess(random):
   # print(random)
    
    for i in range(10):
        print("guess one three character word")
        print("current guess count: "+ str(i) + "/5")
        guess = input()

        if str(guess)== str(random):
            print("yay you got it")
            return i
        else:
            guess = list(guess)
            print(guess[0])
            random = list(random)
            print(random[0])
            if guess[0] == random[0]:
                print("you got the first character right")
            if guess[1] == random[1]:
                print("you got the second character right")
            if guess[2] == random[2]:
                print("you got the third character right")
            print("try again!")
            guess = str(guess)
            random = str(random)

guess(random)