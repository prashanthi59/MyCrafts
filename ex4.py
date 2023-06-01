import random
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print('please type a number larger then 0 next time')
        quit()
else:
  print('please type a number next time')
  quit()

random_number = random.randint(0,top_of_range)
while True:
    
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time')
        continue
    if user_guess == random_number:
      print("You got it!")
      break
    else:
      
     if user_guess > random_number:
         print("we were  above the number!")
     else:
         print("we were  below the number!")
