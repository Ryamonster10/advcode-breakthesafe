import random
import time as t

print("HELLO, AGENT AL. IEN")
print("HACK NASA, AND STEAL THEIR SECRETS")

code = []
for i in range(0,4):
  code.append(random.randint(0,9))
  

cOde = str(code[1]) + str(code[2]) + str(code[3])
for i in range(0,1000):
  guess = input("Type a 3-digit code or 'hack' to get a num")
  if str(guess) == "hack":
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    guessy =  input("whats " + str(num1) + "+" + str(num2))
    if int(guessy) == num1 + num2:
      print("GOOD! THERE IS A " + str(code[random.randint(1,3)]))
    else:
      print("NO LOL")
  if str(guess) == cOde:
      print("NASA HACKED!")
      print("LET'S SEE THEIR SECRETS!")
      for i in range(1,4):
          print("."*i)
          t.sleep(2)
      print("UM...So...yeah")
      t.sleep(4)
      print("its literally just Rick Astley")
      break