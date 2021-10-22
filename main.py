import random
lowNumber = input("enter a low number ")
highNumber = input("enter a high number ")

lives = 5
storednumber = random.randint(int(lowNumber),int(highNumber))
print("My random number generator")

while lives > 0:
  userguess =int( input("enter a number "))
 
  if userguess > storednumber:
    print("Your guess is too big!")
    lives -= 1
    print(lives)
  if userguess < storednumber:
    print("Your guess is too small!")
    lives -= 1
    print(lives)
  if userguess == storednumber:
    break  
print(storednumber)  
if lives == 0:
  print("You lose")
else:
  print("You win")




 